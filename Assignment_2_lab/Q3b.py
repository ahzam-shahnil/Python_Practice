def final_digits_sum_string(num, n):
    le = []
    st = str(num)
    i = 0

    # we are filling the list with dummy range list for further use
    ls = [*range(n)]
    j = n - 1

    while i < len(st):

        # this loop is for setting the indexes according to given number and iterating the indexes
        while j >= 0:
            if len(ls) < n:
                ls.append(i + j)
            else:
                ls[j] = i + j
            j -= 1
        # we use first and last index to slice the string accordingly
        first_index = int(ls[0])
        last_index = int(ls[n - 1])

        if last_index < len(st):
            le.append(final_digits_sum(st[first_index: last_index + 1: 1]))
        # to iterate the index loop we reset j
        j = n - 1
        i += 1
    print(f"Final Answer is {le}")


def final_digits_sum(num):
    print(f"===> Given Number is {num} <===")
    str_num = str(num)
    sum_n = 0
    output = ""
    i = 0
    while i < len(str_num):

        if i == len(str_num) - 1:
            output = output + str_num[i] + " ="
        else:
            output = output + str_num[i] + "+"
        sum_n += int(str_num[i])

        if i == len(str_num) - 1:
            str_num = str(sum_n)
            print(f"{output} {sum_n}")
            if len(str_num) == 1:
                print(f"-->Result is {str_num}")
                break
            else:
                i = -1
                output = ""
                sum_n = 0

        i += 1
    return int(str_num)


nums = 86586247
niter = 4
print(f"--->> The original number is {nums} <<---")
print(f"--->> The  number of pair is {niter} <<---")
final_digits_sum_string(num=nums, n=niter)
