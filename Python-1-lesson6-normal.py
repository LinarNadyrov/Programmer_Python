# coding: utf-8  

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

# К сожалению ранее данную игру не писал, не могу понять в чем ее суть. 
class Person (): 
    def __init__ (self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor


class Player (Person):
    def __init__(self, name, health, damage, armor): 
        super().__init__(name, health, damage, armor)

    def one (self):
        pass

    def two (self):
        pass



class Enemy (Person):
    def __init__(self, name, health, damage, armor): 
        super().__init__(name, health, damage, armor)

    def one (self):
        pass

    def two (self):
        pass