# age = int(input())
# if age <= 14:
#     print('drink toddy')
# elif 14 < age <= 18:
#     print('drink coke')
# elif 18 < age <= 21:
#     print('drink beer')
# else:
#     print('drink whisky')
age = int(input())
drink = '0'
if age <= 14:
    drink = 'toddy'
elif age <= 18:
    drink = 'coke'
elif age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'
print(f'drink {drink}')