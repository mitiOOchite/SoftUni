day_number = int(input())

if day_number < 6:
    weekend_or_working_day = "Working Day"
elif 6 < day_number <= 7:
    weekend_or_working_day = "Weekend"
else:
    weekend_or_working_day = "Error"

if day_number == 1:
    print(f"Monday {weekend_or_working_day}")
elif day_number == 2:
    print(f"Tuesday {weekend_or_working_day}")
elif day_number == 3:
    print(f"Wednesday {weekend_or_working_day}")
elif day_number == 4:
    print(f"Thursday {weekend_or_working_day}")
elif day_number == 5:
    print(f"Friday {weekend_or_working_day}")
elif day_number == 6:
    print(f"Saturday {weekend_or_working_day}")
elif day_number == 7:
    print(f"Sunday {weekend_or_working_day}")
else:
    print(f"Error {weekend_or_working_day}")
