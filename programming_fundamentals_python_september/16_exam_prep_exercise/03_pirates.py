command = input()
town_dict = {}
while command != "Sail":
    town, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if town not in town_dict:
        town_dict[town] = {"population": population, "gold": gold}
    else:
        town_dict[town]['population'] += population
        town_dict[town]['gold'] += gold
    command = input()
command = input().split("=>")
while command[0] != "End":
    if command[0] == 'Plunder':
        current_town, people, current_gold = command[1], int(command[2]), int(command[3])
        if current_town in town_dict:
            town_dict[current_town]['population'] -= people
            town_dict[current_town]['gold'] -= current_gold
            print(f"{current_town} plundered! {current_gold} gold stolen, {people} citizens killed.")
            if town_dict[current_town]['gold']<=0 or town_dict[current_town]['population'] <= 0:
                print(f"{current_town} has been wiped off the map!")
                town_dict.pop(current_town)
    elif command[0] == 'Prosper':
        current_town, current_gold = command[1], int(command[2])
        if current_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            town_dict[current_town]['gold'] += current_gold
            print(f"{current_gold} gold added to the city treasury. {current_town} now has {town_dict[current_town]['gold']} gold.")
    command = input().split("=>")
if len(town_dict) > 0:
    print(f'Ahoy, Captain! There are {len(town_dict)} wealthy settlements to go to:')
    for remaining_towns,values in town_dict.items():
        print(f"{remaining_towns} -> Population: {town_dict[remaining_towns]['population']} citizens, Gold: {town_dict[remaining_towns]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")