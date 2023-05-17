tel = {'Andrea': 4351, 'Gill': 3506}

tel["Ivan"] = 3483
print(tel)

print(tel.get('Andrea'))

print(tel.keys())

for key_items in tel:
    print(key_items)

tel["Ivan"] +=939
print(tel)

print(tel.get('Roy'))

print(tel.values())

for value_items in tel:
    print(tel.get(value_items))

if "Andrea" in tel:
    print("Andrea is in Dictionary")
