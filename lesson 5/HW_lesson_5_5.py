# 5.
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

file = open('text_5.txt', 'w')
numbers = input('Введите числа через пробел: ')
print(numbers)
file.write(numbers)
file.close()

file = open('text_5.txt', 'r')
numbers = numbers.split()
print(numbers)
summ = 0
for number in numbers:
    summ += int(number)
print(summ)
file.close()
