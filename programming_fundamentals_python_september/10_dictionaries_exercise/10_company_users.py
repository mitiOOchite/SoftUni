command = input()
company_dict = {}
while command != 'End':
    company, ID = command.split(" -> ")
    if company not in company_dict:
        company_dict[company] = [ID]
    else:
        if ID not in company_dict[company]:
            company_dict[company].append(ID)
    command = input()
for key, value in company_dict.items():
    print(key)
    for current_value in value:
        print(f'-- {current_value}')
