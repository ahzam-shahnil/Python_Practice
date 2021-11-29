mat = [[1, 2, 5], [3.5, 5, 4, 444, 666], [133.1, 4, 22]]
max_num = mat[0][0]
for ls in mat:
    for item in ls:
        if(max_num < item):
            max_num = item
print(f"Max number is {max_num}")
