def odd_even_sum(num: str):
    sum_of_odd = 0
    sum_of_even = 0
    for current_num in num:
        if int(current_num) % 2 == 0:
            sum_of_even += int(current_num)
        else:
            sum_of_odd += int(current_num)
    return sum_of_even, sum_of_odd


number = input()
sum_of_even_digits, sum_of_odd_digits = odd_even_sum(number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
