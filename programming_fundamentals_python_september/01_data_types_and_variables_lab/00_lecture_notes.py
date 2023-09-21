# lst = ['mercedes', 'bmw', 'audi']
# for i in range(len(lst)):
#     print(i)
# var = complex(5, 7)
# print('Output:', var)# Output: (5+7j)

# from decimal import Decimal

# a = Decimal('0.1')
# b = Decimal('0.1')
# c = Decimal('0.1')
# print(a + b + c)

# var = 42
# print(type(var))
# var = 'bar'
# print(type(var))
# var = True
# print(type(var))
# print(isinstance(var, bool))
string = 'SoftUni'


def process_data(data):  # this is how we create a function
    if isinstance(data, int):
        print('Processing an integer:', data)
    elif isinstance(data, str):
        print('Processing a string:', data)
    else:
        print('Unknown')


process_data(42)
process_data('Hello')
process_data(['Mitko', 'Joro', 'KolIU'])
new_string = string.replace('SoftUni', 'Python')
print("You're", string)
print('You\'re', new_string)

