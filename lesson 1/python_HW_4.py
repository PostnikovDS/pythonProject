# 4.
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input("Введите целое положительное число: "))
max_number = 0

while user_number != 0:
    num = user_number % 10
    if num > max_number:
        max_number = num
    user_number = user_number // 10

print(max_number)
