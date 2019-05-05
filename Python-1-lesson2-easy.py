# coding: utf-8 

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

A = ["яблоко", "банан", "киви", "арбуз"]
print("Дано: ", A)
print("Вывод:")
for num, frut in enumerate (A):
    print (str(num+1) + '.  {:>8}'.format(frut)) 
    # < — выравнивание по левому краю;
    # ^ — выравнивание по центру;
    # > — выравнивание по правому краю;

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

#print("Удалите из первого списка элементы, присутствующие во втором списке.")
A = [ i*i for i in range(1,10) ]
B = [ i for i in range(1,10) ]
print("Первый список:\n",A)
print("Второй список:\n",B)
for i in A:
    for y in B:
        if i == y:
            c = i 
            A.remove(c)
print("После удаления, первый список: \n", A)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

A = [ i for i in range(1,11) ]
B = [] # Чистый список 
print("Произвольный список из целых чисел:\n",A)
for i in A: 
    if i % 2 == 0: # Проверяем кратность к 2
        B.append(i / 4) # Добавляем в конец нового списка с ()
    elif i % 2 != 0: # Иначае не кратно 2 
        B.append(i*2) # Добавляем в конец нового списка с ()
print("Новый список:\n",B)
