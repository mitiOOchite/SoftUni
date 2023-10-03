my_list = [1, 7, 2, 3, 5, 19, 23]
my_list_with_strings = ['Sofia', 'Pesho', 'tarator','abc']
print(sorted(my_list))
my_list.sort(reverse=False)
print(my_list)
my_list_with_strings.sort(reverse=False) #string sorting prioritize capital lettere
print(my_list_with_strings)
deleted_number = my_list.pop()
print(my_list)
print(deleted_number)