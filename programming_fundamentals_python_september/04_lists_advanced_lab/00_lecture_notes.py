nums = [1, 2, 2, 3, 3, 3, 4, 5]

squares = [num for num in nums if num % 2 == 0]
print(squares)

letters = ['a', 'b', 'c', 'd']

uppercase = [letter.upper() for letter in letters]
print(uppercase)

squared_dict = {num: num ** 2 for num in nums}
print(squared_dict)

even_set = {num for num in nums if num % 2 == 0}
print(even_set)

result = [num ** 2 if num % 2 == 0 else num ** 4 for num in nums]
print(result)