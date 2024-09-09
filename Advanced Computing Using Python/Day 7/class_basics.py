class Car:

    wheels = 4
    model = ""
    make = ""
    year = ""

    def __init__(self,model1, make1, year1):
        self.model = model1
        self.make = make1
        self.year = year1
    def display(self):
        print(f"The model of the car is {self.model}. Make: {self.make} Year: {self.year}")

    def drive(self):
        print(f"{self}Engine running...")


car1 = Car("Honda", "Civic", "2016")
# car1.model = "Honda"
# car1.make = "Corolla"
# car1.year = "2016"

car2 = Car("Toyota", "Corolla", "2020")
# car2.model = "Toyota"
# car2.make = "Inova"
# car2.year = "2017"

car1.display()
car2.display()

car1.drive()
car2.drive()