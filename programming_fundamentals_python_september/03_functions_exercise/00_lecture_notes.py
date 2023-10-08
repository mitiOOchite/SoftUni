# help(filter)
# number = int(input())
# for current_number in range(1, number):
#     number *= current_number
# print(number)
some_num = int(input())
new_num = str(some_num)[::-1]
if some_num == int(new_num):
    print(some_num,new_num)
else:
    print('N0')