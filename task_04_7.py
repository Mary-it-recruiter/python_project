"""
Задание 4.
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str()
 для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для
реализации операции сложения двух объектов класса Matrix (двух матриц).
 Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д.
"""

import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


#    @property
#    def test(self, other=[[1,2,4],[3,4,5],[5,6,6]]):
#        res = self.matrix.copy()
#        for i in range(len(self.matrix)):
#            for k in range(len(self.matrix[i])):
#               res[i][k] = self.matrix[i][k] + other[i][k]
#       print(res)


l1 = [[1, 2, 4], [3, 4, 5], [5, 6, 6]]
l2 = [[11, 21, 41], [31, 41, 51], [51, 61, 61]]
m = Matrix(l1)
s = Matrix(l2)
print(m)
z = m + s
print('z ')
print(z)
print(type(z))
