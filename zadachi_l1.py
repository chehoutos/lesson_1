# Задача № 1

# Поработайте, с переменными, создайте несколько, выведити на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран

# a = 1
# b = 2
# c = a + b
# print(c)
# pet = input("Ваше любимое животное? ")
# color = input("Ваш любимый цвет? ")
# age = input(" Ваше любимое число ")
# print(f"Для Вас эксклюзив {pet} {color} за {age} рублей")


# Задача № 2

# time = int(input("введите время в секундах "))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print("%02d %02d %02d" % (hours, minutes, seconds))


# Задача 3

# n = int(input("введите цифру от 1 до 9 "))
# temp = str(n)
# t1 = temp + temp
# t2 = temp + temp + temp
# result = n + int(t1) + int(t2)
# print(result)


# Задача № 4

# n = abs(int(input("Введите целое положительное число ")))
# max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n >= 1:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max)
#         break

# Вариант № 2

# n = int(input("Введите целое положительное число "))
# max1 = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max1:
#         max1 = n % 10
#     elif n > 9:
#         pass
# print("Максимальное цифра в числе ", max1)


# Задача 5

# profit = float(input("Какая выручка у фирмы? "))
# expenses = float(input("Какие расходы у фирмы? "))
# if profit > expenses:
#     print(f"фирма прибыльная. Рентабельность фирмы {profit / expenses}")
#     workers = float(input("укажите число сотрудников "))
#     print(f"прибыль фирмы на одного сотрудника составляет {profit / workers}")
# elif profit == expenses:
#     print("Фирма работает в ноль")
# else:
#     print("фирма работает в убыток")


# Задача № 6

# a = int(input("Результат спортсмена в первый день? "))
# b = int(input("какой результат спортсмен хочет достигнуть? "))
# day = 1
# km = a
# while a < b:
#     print(f"%d день" % day, a)
#     a = a + 0.1 * a
#     day = day + 1
#     km = km + a
# print(f"%d день" % day, a)
# print(f"Результат спортсмена будет достигнут на %d день" % day)





