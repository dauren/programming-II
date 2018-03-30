from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import json
def save_card(user_id, card_no):
    user_id = str(user_id)
    data = {}
    with open('cards.json', 'r') as file:
        data = json.load(file)
    if data.get(user_id) is not None:
        l = data[user_id]
        if card_no not in l:
            l.append(card_no)
            data[user_id] = l
    else:
        data[user_id] = [card_no]
    with open('cards.json', 'w') as file:
        json.dump(data, file)

def get_cards(user_id):
    user_id = str(user_id)
    data = {}
    with open('cards.json', 'r') as file:
        data = json.load(file)
    if data.get(user_id):
        return data[user_id]
    return []

import logging
from onay import get_balance
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CARD_TYPE, CARD_NO= range(2)

card_prefix = {
    'Единая': '96431085033',
    'Студент': '96439085033',
    'Школьник': '96439085033',
    'Социальная': '96439085033'
}

user_state = {}

def add(bot, update):
    reply_keyboard = [['Единая', 'Студент'], ['Школьник', 'Социальная']]
    update.message.reply_text(
        'Чтобы добавить карту Онай выберите тип карты',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return CARD_TYPE


def card_type(bot, update):
    global user_state
    user = update.message.from_user
    text = update.message.text
    cp = card_prefix.get(text)
    user_state[user.id] = {
        'card_prefix': cp
    }
    update.message.reply_text('Введите последние 8 цифр вашей карты',
                              reply_markup=ReplyKeyboardRemove())
    return CARD_NO


def card_no(bot, update):
    user = update.message.from_user
    card_prefix = user_state[user.id]["card_prefix"]
    cn = card_prefix + update.message.text
    balance = get_balance(cn)
    if balance is None:
        update.message.reply_text('Карта не существует. Попробуйте еще раз')
        return CARD_NO
    save_card(user.id, cn)
    update.message.reply_text('Спасибо баланс вашей карты %d тг' % balance)
    return ConversationHandler.END


def balance(bot, update):
    user = update.message.from_user
    cards = get_cards(user.id)
    reply_keyboard = []
    for c in cards:
        reply_keyboard.append([c])
    update.message.reply_text(
        'Чтобы проверить баланс, выберите свою карту',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

def check_balance(bot, update):
    text = update.message.text
    balance = get_balance(text)
    if balance is None:
        update.message.reply_text('Карта не существует. Попробуйте еще раз')
        return None
    update.message.reply_text('Спасибо баланс вашей карты %d тг' % balance)

def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("271801612:AAF_3DZ-QhhFkmi7dAi_TOjkPw5Ok82eINU")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add)],

        states={
            CARD_TYPE: [RegexHandler('^(Единая|Студент|Школьник|Социальная)$', card_type)],

            CARD_NO: [RegexHandler('^\d{8}$', card_no)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    dp.add_handler(CommandHandler('balance', balance))
    dp.add_handler(RegexHandler('^\d{19}$', check_balance))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()