with open('6.txt','r') as ff:
    data = ff.read()

lines = data.splitlines()

def part_one():
    first_line = lines[0].split()
    second_line = lines[1].split()
    third_line = lines[2].split()
    fourth_line = lines[3].split()
    fifth_line = lines[4].split()

    total_operations = len(first_line)
    total = 0
    for i in range(total_operations):
        sub_total = 0
        first = int(first_line[i])
        second = int(second_line[i])
        third = int(third_line[i])
        fourth = int(fourth_line[i])

        if fifth_line[i] == '+':
            sub_total = first + second + third + fourth
        elif fifth_line[i] == '*':
            sub_total = first * second * third * fourth
        total += sub_total
    print(total)

total_operations = len(lines[0])
first = 0
second = 0
third = 0
fourth = 0
operation = ""
total = 0
sub_total = 0

for i in range(total_operations - 1, -1, -1):
    if lines[0][i] == lines[1][i] == lines[2][i] == lines[3][i] ==  lines[4][i] == " ":
        continue
    elif not first:
        first = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
        first = int(first.strip())
    elif not second:
        second = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
        second = int(second.strip())
    elif not third:
        third = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
        third = int(third.strip())
    elif not fourth:
        fourth = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
        fourth = int(fourth.strip())
    if lines[4][i] in ('*', '+'):
        operation = lines[4][i]
    
    if operation:
        if operation == '*':
            first = 1 if not first else first
            second = 1 if not second else second
            third = 1 if not third else third
            fourth = 1 if not fourth else fourth
            sub_total = first * second * third * fourth
        elif operation == "+":
            first = 0 if not first else first
            second = 0 if not second else second
            third = 0 if not third else third
            fourth = 0 if not fourth else fourth
            sub_total = first + second + third + fourth
        total = total + sub_total
        first = second = third = fourth = False
        operation = ""
print (total)


