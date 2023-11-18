import re
#
# text = input('Please input your email: ')
# x = re.search("\w+\W+\w+\W+\w+",text)
# if x:
#     print('True')
# else:
#     print('False')

# regex = '\b\d{1,2}-[A-Z][a-z]{2}-\d{4}\b' validate date format dd-MMM-yyyy
# text = input()
# x = re.findall(regex,text)
# print(x)

mailregex = '^[a-zA-Z0-9_]+@+[a-zA-Z]+\.[a-zA-Z]+'
emails = ['valid123@mail.bg',
'invalid*name@email.bg']
for email in emails:
    if re.match(mailregex, email):
        print(f'{email} is valid')
    else:
        print(f'{email} is invalid')
