import re

sentence = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_])*@([a-z\-]+)(\.[a-z]+)+)\b'
extracted_mails = re.findall(pattern, sentence)
for extracted_email in extracted_mails:
    print(extracted_email[0])
