import re
pattern = r'^(\$|%)([A-Z][a-z]{2,})\1(: )((\[\d+]\|){3})$'
count_of_inputs = int(input())
for current_val in range(count_of_inputs):
    decrypted_message = input()
    if re.search(pattern,decrypted_message):
        value = re.findall(pattern,decrypted_message)[0][1]
        decoded_message = [chr(int(x)) for x in re.findall(r'\d+',decrypted_message)]
        print(f'{value}: {"".join(decoded_message)}')
    else:
        print("Valid message not found!")