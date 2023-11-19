import re
text = 'somesite'
result = re.search(r'some(?=[a-z]+)',text)
print(result.group())
