# odd/even - odd are apartments(A) even are offices(0)
# first one is large apartments L
# L,A, 0
number_of_floors = int(input())
number_of_rooms = int(input())
floor_letter = ""
for current_floor in range(number_of_floors, 0, -1):
    if current_floor == number_of_floors:
        floor_letter = "L"
    elif current_floor % 2 == 0:  # even number
        floor_letter = "O"
    else:
        floor_letter = "A"  # odd number
    for current_room in range(number_of_rooms):  # range - 0 to number of rooms(input value)
        print(f"{floor_letter}{current_floor}{current_room}", end = " ")
    print()