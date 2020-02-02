# # 1)Пользователь вводит свое имя и возраст
# # вывести строку в формате - “Hello {username} your age is {age}”,
# # заменить текст в фигурных скобках на значения введенные пользователем.
#
# username = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {username} your age is {age}")

# # 2)Пользователь вводит число, вывести его в 132 степени
# # и показать его остаток от деления на 3. Вывод должен быть в одну строку с пояснениями.
#
# number = int(input("Enter your number = "))
# print(f"Число в 132 степени {number ** 132}\nОстаток от деления на 3: {number % 3}")

# # 3)Пользователь вводит 2 числа
# # вывести каждую математическую операцию для этих чисел.
# # Каждая новая операция должна быть выведена с новой строки с  пояснением.
#
# first_numb = int(input("Enter first number: "))
# second_numb = int(input("Enter second number: "))
# print(f'Сложение: {first_numb + second_numb}\n'
#       f'Вычитание: {first_numb - second_numb}\n'
#       f'Умножение: {first_numb * second_numb}\n'
#       f'Деление: {first_numb / second_numb}\n'
#       f'Целая часть от деления: {first_numb // second_numb}\n'
#       f'Возведение в степень: {first_numb ** second_numb}\n'
#       f'Остаток от деления: {first_numb % second_numb}\n'
#       f'Преобразование в отрицательное число: {-first_numb}, {-second_numb}\n'
#       f'Увеличение приоритета расчета: {(first_numb + (first_numb - second_numb))}')

# # 4)Пользователь вводит 3 числа,
# # подставить и посчитать формулу: 2a - 8b / (a-b+c). Вывести результат.
# a = int(input('1: '))
# b = int(input('2: '))
# c = int(input('3: '))
# d = 2*a - 8*b / (a - b + c)
# print(d)

# # 5)Пользователь вводит строку и число,
# # вывести повторение строки равное введенному числу.
# # Вывод должен быть в одну строку.
#
# line = input('Line: ')
# number = int(input('Number: '))
# print(line * number)

# # 6)Даны числа 125 и 437 вывести их остатки от деления на 2, 3, 10, 22 с пояснениями.
# int_1 = 125
# int_2 = 437
# print(f'Остаток от деления числа {int_1} на:\n'
#       f"2  => {int_1 % 2}\n"
#       f"3 => {int_1 % 3}\n"
#       f"10 => {int_1 % 10}\n"
#       f"22 => {int_1 % 22}\n")
#
# print(f'Остаток от деления числа {int_2} на:\n'
#       f"2  => {int_2 % 2}\n"
#       f"3 => {int_2 % 3}\n"
#       f"10 => {int_2 % 10}\n"
#       f"22 => {int_2 % 22}\n")

# # 7)Пользователь вводит 2 числа, вывести целую часть от деления одного на другое.
# numb_1 = int(input('1: '))
# numb_2 = int(input('2: '))
# print(numb_1 // numb_2)

# # 8)Пользователь  вводит 3 строки.
# # Вывести их в одну строку разделенные пробелом.
# # В этой задаче метод print может принимать только один параметр.
#
# str_first = input("Input first string: ")
# str_second = input("Input second string: ")
# str_third = input("Input third string: ")
# print(str_first + " " + str_second + " " + str_third)

# # 9)Даны два числа first = 15 second = 43, записать first в second, a second в first. Вывести
# first = 15
# second = 43
# first, second = second, first
# print(first)
# print(second)
