import re

# text = input()
# regex  = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
# matches = re.findall(regex,text)
# print(" ".join(matches))

mailregex = '^[a-zA-Z0-9_]+@+[a-zA-Z]+\.[a-zA-Z]+'
emails = ['valid123@mail.bg',
'invalid*name@email.bg']
for email in emails:
    if re.match(mailregex, email):
        print(f'{email} is valid')
    else:
        print(f'{email} is invalid')