
from abc import ABC, abstractmethod

class SmartDevice(ABC):

    _name = "Abstract class"
    _status = 'off'

    # def __init__(self):
    #     print("Abstract class Initiated")

    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

    def device_info(self):
        print(f"Device: {self._name}\nStatus: {self._status}")

class SmartLight(SmartDevice):

    def __init__(self, name):
        # print(f"before assignment: {self._name}")
        self._name = name
        self._status = super()._status
        print(f"(Initiator) name: {self._name}, status: {self._status}")
        self.brightness = 50

    @classmethod
    def test(cls):
        print(cls._name)

    def device_info(self):
        print(f"anything")

    def turnOn(self):
        self._status = 'On'
        print("Smart Light is On now")

    def turnOff(self):
        self._status = 'off'
        print("Smarti Light is Off now")

    # def device_info(self):
    #     print(f"This is a smart Light, name of device is {self._name}", end = " ")
    #     print('it is off now' if self._status == 'off' else 'it is on now')

    def set_brightness(self, lvl):
        if not 0 <= lvl <= 100:
            return
        self.brightness = lvl
        print(f"the brightness of {self._name} is set to {lvl}")


# x = SmartDevice()

l = SmartLight('Smart Light 15')
l.device_info()
l.turnOn()
l.device_info()
l.set_brightness(42)

SmartLight.test()


