my_list = [1, 7, 2, 3, 5, 19, 23]
my_list_with_strings = ['Sofia', 'Pesho', 'tarator','Tosho', 'tosho']
print(sorted(my_list))
my_list.sort(reverse=False)
print(my_list)
my_list_with_strings.sort(reverse=False) #string sorting prioritize capital letters
print(my_list_with_strings)
deleted_number = my_list.pop(1) #we can also use indexing in pop to delete based on the index
print(my_list)
print(deleted_number)
index = 2
element = 'Tarator'
my_list.insert(index, element) #insert the value on the specified index
print(my_list)
my_list = my_list[::-1]
print(my_list)
print(*my_list)#prints without square brackets and ''
new_list  = ['Sofia', 'Pesho', 'tarator','Tosho', 'tosho']
new_list[1],new_list[3] = new_list[3],new_list[1]
print(new_list)