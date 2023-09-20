width = int(input())
length = int(input())
height = int(input())
total_space = width * length * height
left_space = total_space
command = input()

while command != "Done":  # Done or integer as string from the input
    current_box = int(command)
    left_space -= current_box
    if left_space <= 0:  # has a negative value of the space that is not enough
        break
    command = input()
if command == "Done":
    print(f"{left_space} Cubic meters left.")
else:
    print(f"No more free space, you need {abs(left_space)} Cubic meters more.")
