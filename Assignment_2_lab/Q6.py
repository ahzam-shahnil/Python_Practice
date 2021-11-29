def reshape_lst(lst_num, numC):
    if len(lst_num) % numC == 0:
        le = []
        i = 0
        while numC * (i + 1) <= len(lst_num):
            if i < len(lst_num):
                x = slice(numC * i, numC * (i + 1), 1)
                le.append(lst_num[x])
            i += 1
        return le
    else:
        print("Invalid row length")


lst = [0,1, 2, 3, 4, 5, 6,7,8]
print(f"Original Matrix is {lst}")
ncols = int(input("Enter Number of Columns for List: "))
lst = reshape_lst(lst_num=lst, numC=ncols)
if lst:
    print(f"--->> After Reshaping the length List is {lst} <<---")
