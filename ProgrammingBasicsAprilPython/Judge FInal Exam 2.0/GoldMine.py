number_of_locations = int(input())
total_amount = 0
for number in range(1,number_of_locations+1):
    total_amount = 0
    expected_harvest = int(input())
    harvest_days = int(input())
    for day in range(1,harvest_days+1):
        daily_harvest = int(input())
        total_amount += daily_harvest
    if day == harvest_days:
        average_gold = total_amount / harvest_days
        if average_gold >= expected_harvest:
            print(f"Good job! Average gold per day: {average_gold:.2f}.")
        else:
            needed_gold = abs(expected_harvest-average_gold)
            print(f"You need {needed_gold:.2f} gold.")
