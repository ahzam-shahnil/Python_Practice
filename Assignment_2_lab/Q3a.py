def final_digits_sum(num):
    st = str(num)
    sum_n = 0
    output = ""
    i = 0
    while i < len(st):

        if i == len(st) - 1:
            output = output + st[i] + " ="
        else:
            output = output + st[i] + "+"
        sum_n += int(st[i])

        if i == len(st) - 1:
            st = str(sum_n)
            print(f"{output} {sum_n}")
            if len(st) == 1:
                break
            else:
                i = -1
                output = ""
                sum_n = 0

        i += 1
    return st


res = final_digits_sum(454545)
print(f"Final Number is {res}")
