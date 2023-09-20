# Първоначално от конзолата се прочита едно число – брой локации – цяло число в интервала [1.. 100]
# За всяка една локация се четат две числа, по едно на ред:
# 1.	На първия ред – очакван среден добив на ден злато – реално число в интервала [0.00.. 10000.00]
# 2.	На втория ред – брой дни, в който ще се копае на дадената локация – цяло число в интервала [1.. 30]
# За всеки ден се чете по едно число:
# •	Добито злато за деня – реално число в интервала [0.00.. 1000.00]
number_of_locations = int(input())
expected_harvest = int(input())
harvest_days = int(input())
total_amount = 0
for number in range(1,number_of_locations+1):
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
    expected_harvest = int(input())
    harvest_days = int(input())
    total_amount = 0
# •	Ако средният добив злато за ден достига или надвишава очаквания среден добив на ден злато:
# o	"Good job! Average gold per day: {среден добив на ден за дадената локация}."
# •	Ако средният добив злато за ден е под очаквания среден добив на ден злато:
# o	"You need {злато, което не е достигнало за достигане на очакваният среден добив} gold."
