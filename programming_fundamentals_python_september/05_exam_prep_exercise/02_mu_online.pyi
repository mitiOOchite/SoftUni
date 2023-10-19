def potion(health, heal):
    heal = rooms[1]
    if health+heal < health:
        health+=heal
        print(f'You healed for 10 hp. Current health: 80 hp.')
        exit()

health = 100
start_bitcoins = 0
rooms = input().split('|')
while health > 0:
    if rooms[0] == 'potion':
        heal = rooms[1]
        potion(health,heal)
