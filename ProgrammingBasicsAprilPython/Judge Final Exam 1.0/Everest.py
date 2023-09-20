END_COMMAND = "END"
command = input()
total_meters = 0
base_meters = 5364
peek_height = 8849
current_meters = 0
day = 1
max_days = 5
while command != END_COMMAND:
    day = day
    while day <= max_days:
        if day == 1:
            current_meters = base_meters
            total_meters = current_meters
        if command == END_COMMAND:
            break
            if total_meters >= peek_height:
                break
        elif command == "Yes" and day <= 5 and total_meters<peek_height:
            day +=1
            current_meters = total_meters
            climbed_meters = int(input())
            total_meters += climbed_meters
            if total_meters >= peek_height:
                break
            elif day == max_days:
                break
            command = input()
        elif command == "No" and day <= 5 and total_meters<peek_height:
            day = day
            climbed_meters = int(input())
            total_meters += climbed_meters
            if total_meters >= peek_height:
                break
            elif day == max_days:
                break
            command = input()
    current_meters = total_meters
    if total_meters >= peek_height:
        print(f"Goal reached for {day} days!")
    else:
        print(f"Failed!")
        print(total_meters)
