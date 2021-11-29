a = input("Please enter a number:\n")
sumNum = 0
while len(a) > 1:
    for x in a:
        sumNum = sumNum + int(x)
    if len(str(sumNum)) > 1:
        print(sumNum)
        a = str(sumNum)
        sumNum = 0
    else:
        break
print(f"Value of a={sumNum}\n")
