
class MusicalInstrument:

    def __init__(self, name, type):
        self._name = name
        self._type = type
        self._is_tuned = True

    def play(self):
        print(f"\nThe {self._name} has been played. ")

    def tune(self):
        self._is_tuned = True
        print(f"\nThe {self._name} has been tuned")

    def check_tuning(self):
        if self._is_tuned:
            print(f"The {self._name} is Tuned")
        else:
            print(f"The {self._name} is Not Tuned")

    @property
    def name(self):
        # print('getter has been called')
        return self._name

    @property
    def type(self):
        return self._type

    @name.setter
    def name(self, new_name):
        # print('Setter has been called')
        self._name = new_name

    @type.setter
    def type(self, new_type):
        self._type = new_type

class Guitar(MusicalInstrument):
    def __init__(self, name, type, strings):
        super().__init__(name, type)
        self.no_of_strings = strings

    def play(self):
        print(f"The guitar {self.name} is strumming. ")

class Piano(MusicalInstrument):
    def __init__(self, name, type, keys):
        super().__init__(name, type)
        self.no_of_keys = keys

    def play(self):
        print(f"The piano {self.name} is playing. ")

class Drum(MusicalInstrument):
    def __init__(self, name, type, size):
        super().__init__(name, type)
        self.size_of_drum = size

    def play(self):
        print(f"The drum {self.name} is getting beaten. ")

if __name__ == "__main__":
    pia = Piano('my_pia', 'percussion', 60)
    pia.play()
