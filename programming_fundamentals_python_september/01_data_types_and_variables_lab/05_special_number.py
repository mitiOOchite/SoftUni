number = int(input())
SPECIAL_NUMBER = [5, 7, 11]
for num in range(1, number + 1):
    digits = str(num)
    sum_dig = 0
    for digit in digits:
        sum_dig += int(digit)
    isSpecial = False
    if sum_dig in SPECIAL_NUMBER:
        isSpecial = True
    print(num,isSpecial)


    # if sum_of_digits in SPECIAL_NUMBER:
    #     print(f'{num} -> True')
    # else:
    #     print(f'{num} -> False')
# -41:28