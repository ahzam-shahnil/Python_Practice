a = ["DARPA", "DARR", "ARPRPAZZZRRR"]
num = 0
le = []
for item in a:
    if (len(item) % 3 == 0):
        num = len(item) // 3
        i = 0
        while i < num:
            if (i < len(item)):
                x = slice(3 * i, 3 * (i + 1), 1)
                le.append(item[x])
            i += 1
    elif (len(item) % 2 == 0):
        num = len(item) // 2
        i = 0
        while i < num:
            if (i < len(item)):
                x = slice(i * 2, 2 * (i + 1), 1)
                le.append(item[x])
            i += 1
print(le)
