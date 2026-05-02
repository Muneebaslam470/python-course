class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.model = model
        self.year = year 

    def get_brand(self):
        return self.__brand + "!"     

    def full_name(self):
        return f"{self.__brand} {self.model}" 

class ElectricCar(Car):
    def __init__(self, brand, model, year, electric_battery):
        super().__init__(brand, model, year)
        self.electric_battery = electric_battery 

my_car = Car("Toyota", "Camry", 2020)
my_tesla = ElectricCar("tesla","model S", 2022 , "54Kw")

print(my_tesla.get_brand())

