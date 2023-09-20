PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
DETERGENT_PRICE = 1.20

pens_count = int(input())
markers_count = int(input())
cleaning_material_liters = int(input())
discount_percent = int(input())/100
total_sum = pens_count * PENS_PRICE + markers_count * MARKERS_PRICE + cleaning_material_liters * DETERGENT_PRICE
total_sum_with_discount = total_sum - (total_sum * discount_percent)
print(total_sum_with_discount)
