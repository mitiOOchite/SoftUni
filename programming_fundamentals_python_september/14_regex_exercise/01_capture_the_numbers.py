import re
line = input()
while line:
    pattern = '\d+'
    numbers = re.findall(pattern,line)
    if numbers:
        print(' '.join(numbers),end = ' ')
    line = input()
