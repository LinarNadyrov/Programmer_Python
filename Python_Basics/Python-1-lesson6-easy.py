# coding: utf-8  

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Закомментировал тело задачи
# class TownCar: 
#     def __init__ (self, name, speed, color, is_police):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
    
#     def go (self):
#         return self.name + " " + "поехала"
        
#     def stop (self):
#         return self.name + " " + "остановилась"

#     def turn(self, direction):
#         return self.name + " " + "повернулась" + " " + direction

# class SportCar:
#     def __init__ (self, name, speed, color, is_police):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
    
#     def go (self):
#         return self.name + " " + "поехала"
        
#     def stop (self):
#         return self.name + " " + "остановилась"

#     def turn(self, direction):
#         return self.name + " " + "повернулась" + " " + direction

# class WorkCar:
#     def __init__ (self, name, speed, color, is_police):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
    
#     def go (self):
#         return self.name + " " + "поехала"
        
#     def stop (self):
#         return self.name + " " + "остановилась"

#     def turn(self, direction):
#         return self.name + " " + "повернулась" + " " + direction

# class PoliceCar:
#     def __init__ (self, name, speed, color, is_police):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
    
#     def go (self):
#         return self.name + " " + "поехала"
        
#     def stop (self):
#         return self.name + " " + "остановилась"

#     def turn(self, direction):
#         return self.name + " " + "повернулась" + " " + direction


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar: 
    def __init__ (self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    
    def go (self):
        return self.name + " " + "поехала"
        
    def stop (self):
        return self.name + " " + "остановилась"

    def turn(self, direction):
        return self.name + " " + "повернулась" + " " + direction

class SportCar(TownCar): # Родительский класс помещается в скобки после имени класса.
    def __init__(self, name, speed, color, is_police): # какие атрибуты будут в этом классе
        super().__init__(name, speed, color, is_police) # наследуем атрибуты и методы от родительского класса 

class WorkCar(TownCar):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(TownCar):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

my_car_1 = TownCar ("Honda", "230 km/h ", "Black", "7171")
my_car_2 = SportCar ("Nissan GT", "340 km/h", "Orange", "0007")
my_car_3 = WorkCar ("Kia", "160 km/h", "Red", "14071988")
my_car_4 = PoliceCar ("Dodge", "370 km/h", "White", "02")

# Тесты
print("Машина и цвет: ", my_car_1.name, ",", my_car_1.color, ",", my_car_1.is_police)
print(my_car_1.go())
print(my_car_1.stop())
print(my_car_1.turn("направо"))

print(my_car_2.turn("налево"))

print(my_car_4.name)
print(my_car_4.speed)






        


