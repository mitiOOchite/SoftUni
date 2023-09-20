deposit_amount = float(input())
deposit_period = int(input())
annual_interest_rate = float(input())/100
value = deposit_amount + deposit_period *((deposit_amount*annual_interest_rate)/12)
print(value)