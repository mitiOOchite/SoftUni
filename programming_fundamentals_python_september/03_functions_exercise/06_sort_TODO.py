def sort(num):
    new_list = []
    for current_num in num:
        new_list.append(int(current_num))
    final_list = sorted(new_list,reverse=False)
    print(final_list)
    return final_list

numbers = input().split()
sort(numbers)
