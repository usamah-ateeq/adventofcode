with open('5.txt','r') as ff:
    data = ff.read()

data = data.splitlines()

fresh_ranges = []
ingredient_ids = []

for item in data:
    if "-" in item:
        fresh_ranges.append(item)
    elif item:
        ingredient_ids.append(item)

fresh = 0
for item_id in ingredient_ids:
    item_id = int(item_id)
    for range_ in fresh_ranges:
        start,end = map(int,range_.split("-"))
        if start <= item_id <= end:
            fresh += 1
            break

print(fresh)