import re
line = input()
pattern = r'(w{3}\.[A-Za-z0-9\-]+(\.[a-z]+)+)'

while line:
    valid_links = re.findall(pattern, line)
    if valid_links:
        link = valid_links[0][0]
        print(link)
    line = input()
