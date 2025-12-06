with open('2.txt','r') as ff:
    input_file = ff.read()

input_file = input_file.splitlines()

def is_invalid(row):
    unsafe = 0
    last_item = None
    last_state = None

    for item in row:
        if last_item is None:
            last_item = item
            continue
        action = int(item) - int(last_item)
        if action > 0:
            if action > 3:
                unsafe += 1
                break
            elif last_state == "decrease":
                unsafe += 1
                break
            last_state = "increase"
        if action < 0:
            if action < -3:
                unsafe += 1
                break
            elif last_state == "increase":
                unsafe += 1
                break
            last_state = "decrease"

        if action == 0:
            unsafe += 1
            break
        last_item = item
    return unsafe

def is_valid_after_remove(data):
    if is_invalid(data) == 0:
        return True, None
    for index, _ in enumerate(data):
        trow = data.copy()
        trow.pop(index)
        runsafe = is_invalid(trow)
        if runsafe == 0:
            return True, None
    return False, data

def part_one():
    unsafe=0
    for row in input_file:
        data = row.split()
        runsafe= is_invalid(data) 
        unsafe += runsafe 
    return len(input_file)-unsafe 

def part_two():
    safe = 0
    for row in input_file:
        data = row.split()
        ret, res = is_valid_after_remove(data) 
        if ret:
            safe += 1
        else:
            with open("failed.txt","a") as fs:
                fs.write(f"{res}\n")
    return safe

print(part_two())