
class MusicalInstrument:

    def __init__(self, name, type):
        self._name = name
        self._type = type
        self.__is_tuned = False

    def play(self):
        print(f"\nThe {self._name} has been played. ")

    def tune(self):
        if self.__is_tuned: return
        self.__is_tuned = True
        print(f"\nThe {self._name} has been tuned")

    def check_tuning(self):
        if self.__is_tuned:
            print(f"The {self._name} is Tuned")
            return True
        else:
            print(f"The {self._name} is Not Tuned")
            return False

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

def test_instrument(instrument):
    is_tuned = instrument.check_tuning()
    if not is_tuned:
        instrument.tune()
    instrument.play()

if __name__ == "__main__":

    my_Guitar = Guitar('zenith', 'String', 7)
    my_Guitar.play()

    my_Piano = Piano("Weightless", "keyboard", 80)
    my_Piano.play()

    my_Drum = Drum("Nightshade", "percussion", "Small")
    my_Drum.play()


    test_instrument(my_Guitar)
    test_instrument(my_Piano)
    test_instrument(my_Drum)

    # The code block will raise the Attribute error
    # as we are accessing the private variable of class
    # outside of class, (outside of class -> in a function or method
    #  that does not belong to object)

    print(my_Drum.__is_tuned)
    my_Drum.__is_tuned = False
    print(my_Drum.__is_tuned)
