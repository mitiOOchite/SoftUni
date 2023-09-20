days_left = 5
pocket_money = float(input())
bracelet_profit = float(input())
expenses = float(input())
gift_price = float(input())
# •	Ако са изработени достатъчно пари за подарък:
# o	"Profit: {всички спестени пари} BGN, the gift has been purchased."
# •	Ако са изработени по-малко нужните пари:
# o	"Insufficient money: {сумата, която не достига} BGN."
total_pocket_money = days_left*pocket_money
total_bracelet_profit = days_left*bracelet_profit
total_saved_money = total_pocket_money+total_bracelet_profit
final_amount = total_saved_money-expenses
if final_amount >= gift_price:
    print(f"Profit: {final_amount:.2f} BGN, the gift has been purchased.")
else:
    amount_difference = abs(gift_price-final_amount)
    print(f"Insufficient money: {amount_difference:.2f} BGN.")
