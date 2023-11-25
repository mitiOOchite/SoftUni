import re

number_of_barcodes = int(input())
pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
group_patter = r'\d+'
for n in range(number_of_barcodes):
    barcode = input()
    valid_barcode = re.findall(pattern,barcode)
    group = re.findall(group_patter,barcode)
    if valid_barcode:
        if group:
            print(f'Product group: {"".join(group)}')
        else:
            print(f'Product group: 00')
    else:
        print('Invalid barcode')