day_input = input()
working_list = ["Monday", "Wednesday", "Tuesday", "Thursday", "Friday"]
weekend_list = ["Saturday","Sunday"]
if day_input in working_list:
    print("Working day")
elif day_input in weekend_list:
    print("Weekend")
else:
    print("Error")