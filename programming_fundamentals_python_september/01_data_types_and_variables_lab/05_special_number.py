number = int(input())
SPECIAL_NUMBER = [5, 7, 11]
for num in range(1, number + 1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)
    if sum_of_digits in SPECIAL_NUMBER:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
