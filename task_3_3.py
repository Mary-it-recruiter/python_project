"""3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
 email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456"""


def my_func(name, surname, byear, city, email, phone):
    print(name, surname, byear, city, email, phone)


my_func(name='Mary', surname='Ivanova', byear=1995, city='Msk',
        email='mary@mail.com', phone='8-800-500-45-65')
