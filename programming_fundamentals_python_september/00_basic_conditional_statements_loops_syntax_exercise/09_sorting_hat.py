name = input()
sorted_check = ''

while name != 'Welcome!':
    if name == "Voldemort":
        print('You must not speak of that name!')
        sorted_check = 'false'
        break
    elif len(name) < 5:
        house = 'Gryffindor'
    elif len(name) == 5:
        house = 'Slytherin'
    elif len(name) == 6:
        house = 'Ravenclaw'
    else:
        house = 'Hufflepuff'
    sorted_check = 'true'
    print(f'{name} goes to {house}.')
    name = input()
if sorted_check == 'true':
    print("Welcome to Hogwarts.")
