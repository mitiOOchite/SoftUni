numbers_as_string = input().split()
number_as_digits = []
for number in numbers_as_string:
    number_as_digits.append(int(number))
is_even = lambda x: x % 2 == 0
result = list(filter(is_even,number_as_digits))
print(result)