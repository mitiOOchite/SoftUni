budget = int(input())
total_amount = 0
while True:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
    current_price = float(command)
    if total_amount + current_price > budget:
        print('You went in overdraft!')
        break
    total_amount += current_price