with open('3.txt','r') as ff:
    input_file = ff.read()

data = input_file.splitlines()

def part_one():
    sum_val =0
    for item in data:
        item = item.split("mul")
        for val in item:
            if val.startswith('('):
                try:
                    variables = val[1:val.index(')')].split(',')
                    sum_val += int(variables[0]) * int(variables[1])
                except Exception:
                    continue
    return sum_val


def part_two():
    sum_val =0
    prev_ = "do()"
    for item in data:
        item = item.split("mul")
        for val in item:
            with open('test.txt','a') as fs:
                fs.write(f"{val}\n")
            if val.startswith('(') and "do()" in prev_:
                try:
                    variables = val[1:val.index(')')].split(',')
                    sum_val += int(variables[0]) * int(variables[1])
                except Exception:
                    continue
            if "don't()" in val:
                prev_ = val
            if "do()" in val:
                prev_=val

    return sum_val
print(part_two())
# data = open("test.txt").read().splitlines()

# sum_val = 0
# for val in data:
#     try:
#         variables = val[1:val.index(')')].split(',')
#         sum_val += int(variables[0]) * int(variables[1])
#     except Exception:
#         continue
# print(sum_val)
