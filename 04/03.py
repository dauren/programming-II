import requests
r = requests.get('http://data.egov.kz/api/v2/progress_courses/data?source={"size":100,"from":0}')
print(r.text)