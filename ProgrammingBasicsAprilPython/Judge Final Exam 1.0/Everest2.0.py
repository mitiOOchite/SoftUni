
start_height = 5364
target_height = 8848
current_height = 0
count = 1

# Start the while loop if the current height is less than the target
while True:
    yes_or_no = input()  # check if Atanas wants to sleep before climbing [ command input]
    # at first, we need to set up the break condition if Atanas wants to end tour
    if yes_or_no == "END":
        break

    if yes_or_no == "Yes":
        count += 1  # increase the count, day 2 [ Дали преди изкачването Атанас нощува: Yes -> започва ден 2-ри ]

    height = int(input())  # get the height climbed for the day [ integer input ]
    current_height += height  # add the height climbed to the current height
    # so, for each day we need to check the break conditions
    # # check if the climbed height is greater than the target, if yes break
    if start_height + current_height >= target_height:  # if 5364 + x >= 8848 break
        break
    # # second break condition: check if the climbing days are more than the tour limit
    if count == 5:
        break

    # Print the result according to the conditions
if start_height + current_height < target_height:  # Fail condition
    print("Failed!")
    print(start_height + current_height)
else:  # Success condition
    print(f"Goal reached for {count} days!")
