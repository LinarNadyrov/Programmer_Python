# coding: utf-8 

# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

number = 0
while not 0 < number < 10:
    number=int(input("Введите число, которое больше 0, но меньше 10: "))
    if not 0 < number < 10:
        print("Число не верное."  ,"\n")
    else:
        print('Введеное число в степени 2:',number**2)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

first=int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
first=first+second
second=first-second
first=first-second
print(first)
print(second)

