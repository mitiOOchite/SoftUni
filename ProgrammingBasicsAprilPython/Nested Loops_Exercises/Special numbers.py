# for idx,digit in enumerate(input()): #enumerate takes each element from a string it gives us its index(position) and its value
#     print(idx)
#     print(digit)

number = int(input())
for num in range(1111, 10000): #from 111 to 10K as int
    is_special = True
    num_as_str = str(num) # num as str"1111"
    for _, digit in enumerate(num_as_str):
        current_digit = int(digit) #digit holds each of th position of the value from the input
        if current_digit == 0:
            is_special = False
            break
        if not number % current_digit ==0:
            is_special = False
            break
    if is_special:
        print(f"{num}", end = " ")
