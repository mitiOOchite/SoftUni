import re
dates = input()
regex = '\\b\d{2}/[A-z][a-z]{2}/\d{4}\\b|\\b\d{2}-[A-z][a-z]{2}-\d{4}\\b|\\b\d{2}\.[A-z][a-z]{2}\.\d{4}\\b'
matches = re.findall(regex,dates)
for current_date in matches:
    day,month,year = current_date.split(current_date[2])
    print(f'Day: {day}, Month: {month}, Year: {year}')