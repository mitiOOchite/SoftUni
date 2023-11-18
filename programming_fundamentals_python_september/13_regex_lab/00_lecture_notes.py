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
# # print(x)
#
# mailregex = '^[a-zA-Z0-9_]+@+[a-zA-Z]+\.[a-zA-Z]+'
# emails = ['valid123@mail.bg',
# 'invalid*name@email.bg']
# for email in emails:
#     if re.match(mailregex, email):
#         print(f'{email} is valid')
#     else:
#         print(f'{email} is invalid')

import re
string = 'The quick brown fox jumps over the lazy dog. Python is fun'
match = re.search('\\bp\\w*',string,re.IGNORECASE) #ignores lower or uppercase
if match:
    print(f'The first word that starts with "p" is: {match.group()}')
else:
    print('No words starting with "p"')
"""
# if we use r'' before the regex we dont need to use escape characters 
without them we need the double backslash
"""