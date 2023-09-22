number_of_chars = int(input())
total_sum = 0
for character in range(number_of_chars):
    character = input()
    asci_value = ord(character)
    total_sum += asci_value
print(f'The sum equals: {total_sum}')
