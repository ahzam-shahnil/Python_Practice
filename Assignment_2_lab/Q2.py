def sum_according_to_divisor(ls):
    sum3 = 0
    sum2 = 0
    sum5 = 0
    sum = 0

    for item in ls:
        print(item)
        if item % 2 == 0:
            sum2 += item
        elif item % 3 == 0 and item % 2 != 0:
            sum3 += item
        elif item % 5 == 0 and item % 2 != 0 and item % 3 != 0:
            sum5 += item
        elif item % 5 != 0 and item % 2 != 0 and item % 3 != 0:
            sum += item
    ls[0] = sum2
    ls[1] = sum3
    ls[2] = sum5
    ls[3] = sum
    print(ls)


sum_according_to_divisor([2, 15, 6, 7])
