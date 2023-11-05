command = input()
miner_dict = {}
miner_list = []
while command != 'stop':
    miner_list.append(command)
    command = input()
for current_val in range(0, len(miner_list), 2):
    product = miner_list[current_val]
    quantity = int(miner_list[current_val + 1])
    if product in miner_dict:
        miner_dict[product] += quantity
    else:
        miner_dict[product] = quantity
for key, value in miner_dict.items():
    print(f'{key} -> {value}')
