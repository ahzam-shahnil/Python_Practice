def map_names_to_grades(name_lst, grade_lst):
    i = 0
    student_map = {}
    while i < len(name_lst):
        student_map[f"{name_lst[i]}"] = f"{grade_lst[i]}"
        i += 1
    print(student_map)


names = ["Yossi", "Yafa", "Moti"]
grades = [100, 95, 97]
map_names_to_grades(name_lst=names, grade_lst=grades)
