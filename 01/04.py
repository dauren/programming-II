import winsound
import time
def morse_letter_play(morse):
	frequency = 1500  # Set Frequency To 2500 Hertz
	for item in morse:
		if item == '-':
			duration = 1500  # Set Duration To 1000 ms == 1 second
			winsound.Beep(frequency, duration)
		if item == '.':
			duration = 500  # Set Duration To 1000 ms == 1 second
			winsound.Beep(frequency, duration)
		time.sleep(1.5)

def morse_text_play(text):
	for item in text:
		morse_letter_play(item)

morse_text_play(['.-', '.-..', '..', '-.--', '.-'])
winsound.PlaySound('file.wav', winsound.SND_FILENAME)
