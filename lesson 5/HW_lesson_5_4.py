# 4.
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', 'r') as file:
    for line in file:
        x = line.split()
        new_file.append(f'{translate[x[0]]} — {x[2]} \n')
    print(new_file)

with open('text_4_rus.txt', 'w', encoding='utf-8') as file:
    for line in new_file:
        file.writelines(line)
