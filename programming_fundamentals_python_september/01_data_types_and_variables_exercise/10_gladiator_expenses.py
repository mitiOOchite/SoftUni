lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmets_broken = lost_fights // 2
total_swords_broken = lost_fights // 3
total_shield_broken = lost_fights // (2 * 3)
total_armor_broken = total_shield_broken // 2
expenses = total_swords_broken * sword_price + total_shield_broken * shield_price + total_armor_broken * armor_price + helmet_price * total_helmets_broken
print(f'Gladiator expenses: {expenses:.2f} aureus')