class Car:
    num_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.num_cars += 1

    @classmethod
    def get_number_of_cars(cls):
        return f"total number of cars created: {cls.num_cars}"

    def get_number_class(self):
        return f"total number of cars created: {self.num_cars}"

car1 = Car('b1', 'm1')
print(car1.get_number_of_cars())
print(car1.get_number_class())