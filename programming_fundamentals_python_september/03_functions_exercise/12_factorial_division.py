def calc_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number


num_1 = int(input())
num_2 = int(input())
first_number_factorial = calc_factorial(num_1)
second_number_factorial = calc_factorial(num_2)
result = first_number_factorial / second_number_factorial
print(f'{result:.2f}')