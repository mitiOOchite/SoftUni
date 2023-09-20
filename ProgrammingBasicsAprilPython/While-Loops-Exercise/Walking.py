steps = 0
command = input()
while command != "Going home": #command holds either Going Home or integer as string
    current_steps = int(command)
    steps += current_steps
    if steps >= 10000:
        break
    command = input()
if command == "Going Home":
    current_steps = int(input())
    steps += current_steps
    print(f"")

if steps >= 10000:
    print(f"Goal Reached!")
    print(f"Steps: {steps - 10000} steps over the goal")
else:
    print(f"{10000 - steps} more steps to reach goal")