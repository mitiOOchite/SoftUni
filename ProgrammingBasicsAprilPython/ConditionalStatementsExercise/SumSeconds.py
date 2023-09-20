seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

seconds_sum = seconds_first + seconds_second + seconds_third
# print(seconds_sum)
time_minutes = seconds_sum // 60
time_seconds = seconds_sum % 60
if time_seconds < 10:
    print(f"{time_minutes}:{time_seconds:02d}")
else:
    print(f"{time_minutes}:{time_seconds}")
