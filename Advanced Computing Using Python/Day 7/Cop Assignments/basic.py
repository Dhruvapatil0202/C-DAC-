class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

if __name__ == "__main__":
    per1 = Person('name1', 32)
    per2 = Person('name2', 45)
    print(f"per1: name = {per1._name}, age = {per1._age}")
    print(f"per2: name = {per2._name}, age = {per2._age}")
