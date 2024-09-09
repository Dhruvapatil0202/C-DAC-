class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name
    def get_breed(self):
        return self._breed
    def set_breed(self, new_breed):
        self._breed = new_breed

if __name__ == "__main__":
    my_dog = Dog('cupcake', 'German')
    print(my_dog.get_name())
    my_dog.set_name('Noodle')
    print(my_dog.get_name())

    print(my_dog.get_breed())
    my_dog.set_breed('Golden')
    print(my_dog.get_breed())
    
