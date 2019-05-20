# coding: utf-8  

import sys
import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# создающий директории dir_1 - dir_9 в папке
try:
    for i in range (1, 10):
        os.mkdir("dir_" + str(i))
except FileExistsError:
    print ("Такая директория уже существует")
print(os.listdir(os.getcwd()))

# # удаляющий эти папки
for i in range(1, 10):
        os.removedirs("dir_" + str(i))
print(os.listdir(os.getcwd()))

# # Задача-2:
# # Напишите скрипт, отображающий папки текущей директории.
# Первый вариант
path = os.listdir()
for i in path:
    if os.path.isdir(i):
        print(i)

# Второй вариант
print([i for i in os.listdir() if os.path.isdir(i)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

original_file = sys.argv[0]
print(original_file)
copy_file = original_file + ".copy"
shutil.copy(original_file, copy_file) 