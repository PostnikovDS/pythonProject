# 1.
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('text_1.txt', 'w') as obj_text:
    string = 0
    result = []
    while not string == '':
        string = input('Введите строку: ')
        result.append(f'{string} \n')
    print(result)
    obj_text.writelines(result)

