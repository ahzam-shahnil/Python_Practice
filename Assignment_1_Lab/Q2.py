le = [2, 3]
sum_num = 0
count = 0
for item in le:
    if (item > 3):
        sum_num += item
        count += 1
if (sum_num != 0):
    print(f"Sum is {sum_num}")
    print(f"Avergae of {count} numbers is {sum_num / count}")
else:
    print("Sum is 0")
    print("Avergae is 0")
