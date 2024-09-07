
class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        pass
    def speak(self):
        print("Dog is barking")

if __name__ == "__main__":
    animal = Animal()
    animal.speak()

    the_dog = Dog()
    the_dog.speak()


