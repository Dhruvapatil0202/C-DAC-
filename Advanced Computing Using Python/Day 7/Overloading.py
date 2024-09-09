
from abc import ABC
class Calculator:
    def add(self,*args):
        return sum(args)

calc = Calculator()
print(calc.add(1,3,5))
print(calc.add(0))