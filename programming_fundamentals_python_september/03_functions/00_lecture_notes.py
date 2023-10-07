def sum_numbers():
    a = input()
    b = input()
    print(a+b)
sum_numbers()

#
# for _ in range(3):
#     a = int(input())
#     b = int(input())
#     result = sum_numbers(a,b)
#     print(result)

#Declaring a function with parameters

def greet(name):
    print('Hello,', name)
greet('Maria')


def print_nums_from1_to_n(n):
    for num in range(1, n+1):
        print(num)
print_nums_from1_to_n(5)

def calculate_rectangle_are(lenght, width):
    area = lenght*width
    return area
#Calling the functuion with named paraments
result = calculate_rectangle_are(width=5,lenght=10)
print(result)

def calculate_square(num):
    """
    This function calculates the square of a given number
    :param num: int or float.
    :return: float: The square of the input number
    """
    square = num**2
    return square
    print(square)
help(calculate_square)

def count_numbers(n):
    if n <= 10:
        print(n)
        count_numbers((n+1))
count_numbers(1)


square = lambda x: x**2
print(square(2))
add = lambda a,b: a+b
print(add(2,6))

is_even = lambda a: a%2 == 0
print(is_even(10))