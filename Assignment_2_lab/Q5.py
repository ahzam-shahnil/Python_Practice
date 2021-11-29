def add_scalar_to_mat(ls, num):
    for x in range(len(ls)):
        for y in range(len(ls[x])):
            ls[x][y] = ls[x][y] + num
    return ls


ls = [[1, 2, 3], [4, 5, 6]]
print(f"Original Matrix is {ls}")
num = int(input("Enter number to add to the matrix:"))
ls = add_scalar_to_mat(ls=ls, num=num)
print(f"After Scalar addition matrix is {ls}")
