hours = 0
# while hours < 24, we print hours + minutes at 23:59 we show 0:0
# while minutes < 60, pritn minutes, else hours += 1

# while hours < 24:
#     minutes = 0
#     while minutes < 60:
#         print(f"{hours}:{minutes}")
#         minutes += 1
#     hours += 1
# for hours in range(0,24):
#     for minutes in range(0,60):
#        print(f"{hours:02d}:{minutes:02d}")

for hours in range(24):
    for minutes in range(60):
        print(f"{hours:02d}:{minutes:02d}")