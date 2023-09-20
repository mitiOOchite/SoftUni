# import antigravity
mussala_count = 0
montblanc_count = 0
kilimanjaro = 0
k2_count = 0
everest_count = 0
climbers_group_count = int(input())
for _ in range(climbers_group_count):
    current_climbers = int(input())
    if current_climbers <6:
        mussala_count += current_climbers
    elif current_climbers <13:
        montblanc_count += current_climbers
    elif current_climbers < 26:
        kilimanjaro += current_climbers
    elif current_climbers < 41:
        k2_count += current_climbers
    elif current_climbers >= 41:
        everest_count  = current_climbers
total_climbers = mussala_count + montblanc_count+everest_count+kilimanjaro+k2_count
mussala_percent = mussala_count / total_climbers *100
kilimanjaro = kilimanjaro / total_climbers *100
everest_percent = everest_count / total_climbers *100
k2_percent = k2_count / total_climbers *100
montblanc_percent = montblanc_count / total_climbers * 100

print(f"{mussala_percent:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{everest_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")