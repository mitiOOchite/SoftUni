group_size = int(input())
days = int(input())
coins = 0
current_group_size = group_size
for current_day in range(1, days + 1):
    if 1 < days > 100: #constraints to make sure the days fall within the paraments
        break
    if 1 < group_size > 100:
        break
    if current_day % 10 == 0:  # we need to first check if the day is the 10th day before checking wheter its also the 5th
        current_group_size -= 2
    if current_day % 15 == 0:  # we must check wheter its the 15th day first before checking if its the 5th or 3rd in order to add the people before substracting
        current_group_size += 5
    if current_day % 3 == 0:
        coins -= current_group_size * 3
    if current_day % 5 == 0:
        coins += current_group_size * 20
        if current_day % 3 == 0:
            coins -= current_group_size * 2
    coins += 50
    coins -= current_group_size * 2
coins_per_person = int(coins // current_group_size) #there are no half coins so we need to round down
print(f'{current_group_size} companions received {coins_per_person} coins each.')
