"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

entered_number = int(input('Введите положительное число:'))
n = entered_number
sum_of_numbers = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(f"Сумма чисел n + nn + nnn  = {sum_of_numbers}")
