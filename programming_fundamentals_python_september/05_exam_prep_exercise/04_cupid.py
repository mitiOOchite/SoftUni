houses = [int(house) for house in input().split("@")]
command = input()
current_index = 0

while command != 'Love!':
    jump_length = int(command.split()[1])
    current_index += jump_length
    if current_index not in range(len(houses)):
        current_index = 0
    if houses[current_index] == 0:
        print(f'Place {current_index} already had Valentine\'s day.')
    else:
        houses[current_index]-= 2
        if houses[current_index] == 0:
            print(f'Place {current_index} has Valentine\'s day.')


    command = input()
print(f'Cupid\'s last position was {current_index}.')
if sum(houses) == 0:
    print('Mission was successful.')
else:
    houses = [int(house) for house in houses if int(house) != 0]
    print(f'Cupid has failed {len(houses)} places.')