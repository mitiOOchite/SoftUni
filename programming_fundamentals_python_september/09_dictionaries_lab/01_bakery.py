elements = input().split()
bakery = {}

for i in range(0, len(elements),2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)
for key in bakery.values():
    print(key)
print(bakery)
