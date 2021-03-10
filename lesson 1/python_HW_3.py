# 3.
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = str(input('Введите число: '))

nn = int(n + n)
nnn = int(n + n + n)
n = int(n)

result = n + nn + nnn
print(f'{n} + {nn} + {nnn} = {result}')



