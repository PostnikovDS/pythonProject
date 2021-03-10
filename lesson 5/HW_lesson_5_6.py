# 6.
# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as file:
    i = 0
    digit = []
    for line in file:
        for i in line:
            if not i.isdigit():
                line = line.replace(i, "")
        digit.append(line)
    print(digit)

'''
    subject, lecture, practice, lab = line.split()
    subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')


subj = {}
with open('text_6.txt', 'r') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
'''
