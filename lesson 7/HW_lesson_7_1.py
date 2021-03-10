# 1.
# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

# Примеры матриц вы найдете в методичке.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, mx_list):
        self.mx_list = mx_list

    def __str__(self):
        return f"Матрица {self.mx_list}"

    def __add__(self, other):
        return Matrix([
            [self.mx_list[0][0] + other.mx_list[0][0],
             self.mx_list[0][1] + other.mx_list[0][1],
             self.mx_list[0][2] + other.mx_list[0][2]],

            [self.mx_list[1][0] + other.mx_list[1][0],
             self.mx_list[1][1] + other.mx_list[1][1],
             self.mx_list[1][2] + other.mx_list[1][2]],

            [self.mx_list[2][0] + other.mx_list[2][0],
             self.mx_list[2][1] + other.mx_list[2][1],
             self.mx_list[2][2] + other.mx_list[2][2]]
        ])


mx = Matrix([[2, 3, 6], [8, 4, 1], [5, 9, 7]])
print(mx)
mx_2 = Matrix([[11, 45, 31], [56, 78, 92], [21, 18, 76]])
print(mx_2)
mx_3 = Matrix([[43, 11, 98], [21, 56, 4], [55, 87, 62]])
print(mx_3)

mx_sum = mx + mx_2 + mx_3
print(mx_sum)

'''
def __init__(self, mx_list):
        self.mx_list = mx_list

    def __str__(self):
        return f"Матрица {self.mx_list}"

    def __add__(self, other):
        for el in self.mx_list:
            el[0] + other(el[0])
            el[1] + other(el[1])
            el[2] + other(el[2])


mx = Matrix([[2, 3, 6], [8, 4, 1], [5, 9, 7]])
print(mx)
mx_2 = Matrix([[11, 45, 31], [56, 78, 92], [21, 18, 76]])
print(mx_2)

mx_3 = mx + mx_2
print(mx_3)

##################

    def __init__(self, mx_list):
        self.mx_list = mx_list

    def __init__(self, mx_list):
        self.mx_list = mx_list

    def __str__(self):
        return f"Матрица {self.mx_list}"

    def __add__(self, other):
        mx_3 = [[], [], []]
        for el in self.mx_list:
            for i in el:
                mx_3[el][i] = [el][i] + mx_2[el][i]
                mx_3.append(mx_3[el][i])
        return mx_3


mx = Matrix([[2, 3, 6], [8, 4, 1], [5, 9, 7]])
print(mx)
mx_2 = Matrix([[11, 45, 31], [56, 78, 92], [21, 18, 76]])
print(mx_2)

mx_3 = mx + mx_2
print(mx_3)

##############################

    def __init__(self, mx_list):
        self.mx_list = mx_list

    def __str__(self):
        return f"Матрица {self.mx_list}"

    def __add__(self, other):
        return Matrix([self.mx_list[0] + other.mx_list[0], self.mx_list[1] + other.mx_list[1],
                       self.mx_list[2] + other.mx_list[2]])


mx = Matrix([[2, 3, 6], [8, 4, 1], [5, 9, 7]])
print(mx)
mx_2 = Matrix([[11, 45, 31], [56, 78, 92], [21, 18, 76]])
print(mx_2)

mx_3 = mx + mx_2
print(mx_3)
'''
