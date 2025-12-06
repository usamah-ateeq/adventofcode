with open('1.txt','r') as ff:
    data = ff.read()

data = data.splitlines()
col1 = []
col2 = []
for item in data:
    col1.append(int(item.split()[0]))
    col2.append(int(item.split()[1]))

def part_one():
    col1.sort()
    col2.sort()
    sum_val = 0
    for i in range(0,len(col1)):
        sum_val += abs(col1[i] - col2[i])
    return sum_val

def part_two():
    sum_val = 0
    for item in col1:
        counts = col2.count(item)
        sum_val += (item * counts)
    return sum_val

print(part_two())