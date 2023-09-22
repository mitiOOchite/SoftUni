capacity = 255
refills = int(input())
current_capacity = 0
for fill in range(refills):
    liters = int(input())
    if liters > capacity:
        print('Insufficient capacity!')
        continue
    else:
        capacity -= liters
        current_capacity += liters
print(current_capacity)
