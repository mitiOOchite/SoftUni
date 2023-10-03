data_list = [10, 3.14, "Hello", {'name': 'Ivan', 'age': 25}, [1, 2, 3], True, False]
print(type(data_list))
print(data_list)
print(data_list[4][1])  # take index positions, starting from 0

string = 'Hello'
new_string_list = list(string)
print(new_string_list)
empty_list = list()
print(type(empty_list))
print(list(range(1, 11, 2)))  # we create a list from 1 to 11 with a step of 2
some_text = 'a,b,c,d'
my_list = some_text.split(', ')
print(my_list)
nums = input().split(', ')
print(nums)
nums = list(map(int, input().split(', ')))
my_list = ['a', 'b', 'c']
print('-'.join(my_list))
print('index -1',my_list[-1])
print('index -2',my_list[-2])
print('index -3',my_list[-3])