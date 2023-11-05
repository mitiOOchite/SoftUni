items = {
    'shards': 0, 'fragments': 0, 'motes': 0
}
junk_items = {}
current_items = input().split()
obtained = False

while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items:
            if key not in junk_items:
                junk_items[key] = value
            else:
                junk_items[key] += value
        else:
            items[key] += value
            if items[key] >= 250:
                obtained = True
                items[key] -= 250
                if key == 'shards':
                    print('Shadowmourne obtained!')
                elif key == 'fragments':
                    print('Valanyr obtained!')
                elif key == 'motes':
                    print('Dragonwrath obtained!')
        if obtained:
            break
    if obtained:
        break
    current_items = input().split()
for current_key,current_value in items.items():
    print(f'{current_key}: {current_value}')
for junk_key, junk_value in junk_items.items():
    print(f'{junk_key}: {junk_value}')
