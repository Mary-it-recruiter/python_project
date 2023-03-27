"""
Задание 2.Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
natural_num = input("Введите натуральное число: ")
even_count = 0
odd_count = 0

for number in natural_num:
    if int(number) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Количество четных цифр:", even_count)
print("Количество нечетных цифр:", odd_count)
