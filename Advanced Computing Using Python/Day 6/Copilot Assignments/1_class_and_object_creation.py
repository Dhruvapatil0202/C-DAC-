
"""
Writing a Class
Creating an object of that class
prints out all the attributes of the created object and their values  
"""
class Vehicle:
    def __init__(self, milage: int, top_speed: int):

        self.milage = milage
        self.top_speed = top_speed

if __name__ == "__main__":

    temp_vehicle = Vehicle(45, 700)
    for attribute, value in temp_vehicle.__dict__.items():
        print(f"{attribute} = {value}")


