def is_even(num):
    if num % 2 == 0:
        return True
    return False


numbers_as_string = input().split()
number_as_digits = []
for number in numbers_as_string:
    number_as_digits.append(int(number))
even_numbers = []
for element in number_as_digits:
    if is_even(element):  # if is even == True
        even_numbers.append(element)
print(even_numbers)
