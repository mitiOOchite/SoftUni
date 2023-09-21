year = int(input())

while True:
    year += 1
    year_str = str(year)
    set_value = set(year_str)#splits the value and takes only the unique values if we have 00001 the set will be (0 and 1)
    len_set = len(set(year_str))
    if len(set(year_str)) == len(year_str): #if the number of the unique set values is the same as the numbe of characters as the year it means its a unique year
        break
print(year)