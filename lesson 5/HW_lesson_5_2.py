# 2.
# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('text_2.txt') as file:
    str_count = 0
    words_count = 0
    for line in file:
        print(line, end='>>')
        str_count += 1
        words_count = len(line.split())
        print(f'Строка: {str_count}; Количество слов: {words_count}')

    print(f'Общее количество строк {str_count}')
