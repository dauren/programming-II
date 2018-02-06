import requests
import json
from collections import Counter
r = requests.get('http://data.egov.kz/api/v2/progress_courses/data?source={"size":2000,"from":0}')
data = r.json()
school_stat = Counter()
for course_item in data:
	school_name = course_item['school name']
	course_name = course_item['course']

	if course_item['region'] == 'г.Алматы' and ("математика" in course_name.lower() or "алгебра" in course_name.lower() or "геометрия" in course_name.lower()):
		c = course_item['grade_five']
		school =  school_name + "||" +course_item['region']
		school_stat[school] += c


l = school_stat.most_common(3)
print(l)

