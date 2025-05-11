''' A class is a BLUEPRINT which is used to define attributes and functions of an Object
Objects are made from a Class.eg. object_1=class(), object_2=class()'''
from symtable import Class


class bike:
    def __init__(self,brand,price):
        self.company_ka_naam= brand
        self.paisa= price

bike_1=bike("yamaha","200k")
bike_2=bike("Ninja!","200k")

# print(bike_1.company_ka_naam)
# print(bike_1.paisa)
#
# print(bike_2.company_ka_naam)

''' ⬆️⬆️⬆️⬆️__init__() is a constructor: a special method that runs automatically when you create an object.
self refers to the current object itself.
self.company_ka_naam and self.paisa are attributes saved in each object.
'''

# class car:
#     def __init__(self,brand, model, year):
#         self.company_ka_naam=brand
#         self.model_name=model
#         self.dob=year
# vroom=car("Ferrari","F-12 Spyder.",2022)
# shroom=car("Lamborghini","Roadster SV.",2023)

# print(f"{vroom.company_ka_naam}\n{vroom.model_name}\n{shroom.company_ka_naam}\n{shroom.model_name}")
""" adding actions """
class car:
    def __init__(self,brand, model, year):
        self.company_ka_naam=brand
        self.model_name=model
        self.dob=year
    def honk(self):
        print(f"{self.company_ka_naam} says Beep! Beep! Beep! MadaFakas!!!")
    def display_info(self):
        print(f"{self.company_ka_naam} {self.model_name} is {self.dob} made.")
    def start_engine(self):
        print(f"{self.company_ka_naam} {self.model_name} engine started. vrooom!! move out the way beaches!!!")
    def change_model(self,new_model):
        self.model_name=new_model
        print(f"Model updated to {self.model_name} for {self.company_ka_naam}")

vroom=car("Ferrari","F-12 Spyder",2022)
shroom=car("Lamborghini","Roadster SV",2023)

# vroom.change_model("Purosangue ! ")
# vroom.display_info()
# vroom.honk()
# vroom.display_info()
# shroom.start_engine()

''' Objects can store data (attributes)
    Objects can do actions (methods)
    Methods use self to access that object's data
    You can create many unique objects, all using the same class '''

class ElectricCar(car):
    def __init__(self,brand, model, year,battery_range):
        super().__init__(brand, model, year)
        self.battery_range=battery_range
    def charge(self):
        print(f"Charging {self.company_ka_naam} with range {self.battery_range} km")
    def battery_status(self):
        print(f"Battery status: {self.battery_range} km left in {self.company_ka_naam}")

car_23=ElectricCar("Tesla","Y",2025,250)

car_23.battery_status()
car_23.charge()
car_23.honk()
car_23.display_info()


'''  Inherited from the car class using class ElectricCar(car)
     Used super().__init__() to call the parent constructor
'''


