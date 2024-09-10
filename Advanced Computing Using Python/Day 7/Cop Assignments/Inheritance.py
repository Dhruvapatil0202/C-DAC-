class Vehicle:
    def __init__(self, year, type):
        self._year = year
        self._type = type

class Car(Vehicle):
    def __init__(self, no_of_doors):
        super().__init__(year = 1889, type = 'Family')
        self._no_of_doors = no_of_doors

if __name__ == "__main__":
    my_car = Car(4)
    print(my_car._year, my_car._type, my_car._no_of_doors)
