def switch_couples_in_lst(lst_num, couples_lst_n):
    for x in range(len(lst_num)):
        for i in range(len(couples_lst_n)):
            if lst_num.__contains__(couples_lst_n[i][0]) and lst_num.__contains__(couples_lst_n[i][1]):
                a = lst_num[lst_num.index(couples_lst_n[i][0])]
                b = lst_num[lst_num.index(couples_lst_n[i][1])]
                temp = lst_num.index(couples_lst_n[i][1])
                lst_num[lst_num.index(a)] = b
                lst_num[temp] = a
        break
    return lst_num


#
# lst = [5, 'gorilla', 12, 6.4, 'python']
# couples_lst = [[12, 5], ['python', 12]]
lst = [5, 6, 5, 12]
couples_lst = [[12, 6], [12, 6]]
couples_lst = switch_couples_in_lst(lst, couples_lst)
print(couples_lst)
