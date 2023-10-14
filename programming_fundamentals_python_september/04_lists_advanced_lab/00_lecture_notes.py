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

result = [num ** 2 if num % 2 == 0 else num ** 3 for num in nums]
print(result)

fruits = ['apple', 'banana', 'banana', 'orange', 'banana','date']

counter_of_bananas = fruits.count('banana')
index_of_banana = fruits.index('apple')
print(counter_of_bananas)
print(index_of_banana)


sorted_fruits = sorted(fruits)
print(sorted_fruits)

words = ['programming', 'is', 'super', 'fun', 'Python']
sorted_words = sorted(words, key=len)
print(sorted_words)

names = ['Asen','Ivan', 'Angel', 'Plamen', 'Anu']
filtered_names = list(filter(lambda name: name.startswith('A'), names))
print(filtered_names)

numbers = [1, 2, 3, 4, 5]
index1 = 1
index2 = 3

numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
print(numbers)