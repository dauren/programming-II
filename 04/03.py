import requests
import json
from collections import Counter
r = requests.get('http://data.egov.kz/api/v2/progress_courses/data?source={"size":2000,"from":0}')
data = r.json()
school_stat = Counter()
for course_item in data:
	school_name = course_item['school name']
	grade_two = course_item['grade_two']
	school =  school_name + "||" +course_item['region']
	school_stat[school] += grade_two

print(school_stat)

