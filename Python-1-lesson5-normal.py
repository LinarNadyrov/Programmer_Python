# coding: utf-8  

import sys
import os
import shutil
from add_remove_path import add_path, remove_path

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

print('''
1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку
''')

key = input ("Пожалуйста, выберите действие: ")

if key == "1":
    os.chdir(os.getcwd() + "/" + input("Введите название папки: "))
    print("Вы находитесь в директории: ", os.getcwd())

elif key == '2':
    print("Содержимое данной папки:\n")
    path = os.listdir()
    for i in path:
        print(i)

elif key == '3':
     name_dir = input("Введите название папки которую хотите удалить: ")
     remove_path(name_dir, 2)
     print("Вы удалили: " + name_dir)

elif key == '4':
    name_dir = input("Введите название папки которую хотите создать: ")
    add_path(name_dir, 2)
    print("Вы создали: " + name_dir)