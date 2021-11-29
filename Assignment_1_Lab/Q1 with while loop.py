le = [2, 7, 3, 4454, 5, 6, 1]
max_num = le[0]
i = 0
length = len(le)
while i < length:
    num = le[i]
    if max_num < num:
        max_num = num
    i += 1
print(f"Max Number is {max_num}")
