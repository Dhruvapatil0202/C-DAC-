from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car has started")

    def stop(self):
        print("Car has stopped")


class Bus(Vehicle):

    def start(self):
        print("Bus has started")

    def stop(self):
        print("Bus has stopped")

class Truck(Vehicle):

    def start(self):
        print("Truck has started")

    def stop(self):
        print("Truck has stopped")

class Garage:
    def __init__(self):
        self.parking = []

    def add_vehicles_in_parking(self, *vehicle):
        self.parking.extend(vehicle)

    def operate_vehicle(self, *random_object):

        for vehicle in random_object:

            vehicle.start()
            vehicle.stop()


car = Car()
bus = Bus()
truck = Truck()

# (car.start())
# (car.stop())
#
# (bus.start())
# (bus.stop())
#
# (truck.start())
# (truck.stop())

gar = Garage()

gar.add_vehicles_in_parking(car, bus, truck)
gar.operate_vehicle(car, bus, truck)


