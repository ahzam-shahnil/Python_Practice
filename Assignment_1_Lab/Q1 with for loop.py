le = [2, 7, 3, 444, 5, 6, 1]
max_num = le[0]
for num in le:
    if max_num < num:
        max_num = num
print(f"Max Number is {max_num}")
