def rounding():
    list_values = input().split()
    new_list = []
    for list in list_values:
        new_list.append(round(float(list)))
    result = new_list
    print(result)
rounding()