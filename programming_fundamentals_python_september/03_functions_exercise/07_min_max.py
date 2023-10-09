def min_max_sum(nums):
    num_list = []
    for current_num in nums:
        num_list.append(int(current_num))
    min_num = min(num_list)
    max_num = max(num_list)
    sum_nums = sum(num_list)
    print(f'The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_nums}')
    return min_num,max_num,sum_nums

numbers = input().split()#take input values
min_max_sum(numbers)