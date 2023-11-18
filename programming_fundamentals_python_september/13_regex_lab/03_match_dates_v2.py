# import re
#
# dates = input()
# regex = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
# matches = re.findall(regex, dates)
# for match in matches:
#     day = match[0]
#     month = match[2]
#     year = match[3]
#     print(f'Day: {day}, Month: {month}, Year: {year}')
import re

dates = input()
regex = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
matches = re.finditer(regex, dates)
for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(4)
    print(f'Day: {day}, Month: {month}, Year: {year}')

