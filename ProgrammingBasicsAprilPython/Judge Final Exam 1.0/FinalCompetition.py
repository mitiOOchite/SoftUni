dancers_count = int(input())
points = float(input())
season = input()
country = input()
charity_amount = 0.75
# На конзолата се отпечатват 2 реда:
# •	Сумата, която са дали за благотворителност
# "Charity - {сума за благотворителност}"
# •	Сумата, която е получил всеки танцьор
# "Money per dancer - {сума за танцьор}"

if country == "Bulgaria" and season == "summer":
    reward = dancers_count*points
    expenses = 0.05*reward
    total_reward = reward-expenses
elif country == "Bulgaria" and season == "winter":
    reward = dancers_count*points
    expenses = 0.08*reward
    total_reward = reward-expenses
elif country == "Abroad" and season == "summer":
    reward = dancers_count * points
    final_reward = (0.5*reward)+reward
    expenses = 0.1*final_reward
    total_reward = final_reward-expenses
else:
    reward = dancers_count * points
    final_reward = (0.5 * reward) + reward
    expenses = 0.15 * final_reward
    total_reward = final_reward-expenses
amount_for_chartity = charity_amount*total_reward
final_amount = total_reward-(charity_amount*total_reward)
money_per_dancer = final_amount/dancers_count
print(f"Charity - {amount_for_chartity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")