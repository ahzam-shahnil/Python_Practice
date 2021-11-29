le = [1, 2, 3, 4, 5, 6, 7]
i = 0
flag = True
while i < len(le):
    first = i
    second = i + 1
    check = i + 2
    if (check < len(le)):
        if (le[first] + le[second] != le[check]):
            print(f"Index of check value is {check}")
            flag = False
            break
    i += 1
if (flag):
    print(flag)
