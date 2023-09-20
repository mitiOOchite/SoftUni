length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_non_empty = float(input())/100

total_volume = length_cm * width_cm * height_cm #in cm3

total_volume_in_liters = total_volume / 1000 #1l - 1dm3

water_needed = total_volume_in_liters-(total_volume_in_liters*percent_non_empty)
print(water_needed)