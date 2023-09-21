paper_price = 5.80
linen_price = 7.20
glue_price = 1.20
count_paper = int(input())
count_linen = int(input())
count_glue_per_liter = float(input())
discount = int(input()) / 100
total_price = count_linen * linen_price + count_paper * paper_price + count_glue_per_liter * glue_price
total_price_after_discount = total_price - (discount * total_price)
print(f"{total_price_after_discount:.3f}")
