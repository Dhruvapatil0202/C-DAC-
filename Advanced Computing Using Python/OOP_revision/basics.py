"""
OOP is programming paradigm that models real_world concepts as objects

1. code organisation
2. Data modelling
3. Re-usebility
4. Maintainability

class - custom datatype
1. blueprint for creating objects
2. defines a set of attributes and methods
3. Encapsulate data for resuability and modularity

object - instance of a class
1. Created from the class blueprint
2. Have state and behavior
3. Objects can have different attribute values

Encapsulation - Bundling data and methods so that they operate within a single class
1. improved security
2. better collaboration
3. reduced complexity
4. improved code maintainability
5. constructors
6. getter and setter methods

Class variables:
used to store dat that is shared among all instances of class
defined within a class but outside of any instance methods.
shared among all instance of the class
 any modification to class variable affects every other class variable

Class method:
bound to class than instance
accessed using class names
defined using @classmethod decorator
takes 'cls' : classname as its paramter
used to manipulate data

Static Methods:
used when you want to group utility function within a class
cannot not access or modify class state or instance state
indicated by @staticmethod decorator

Inheritance
Mechanism by which a child class acquires the characteristics of a parent class


Polymorphism
polymorphism is the abiity of method to take on many forms

overriding :
allows the subclass to modify or extend the behavior of the inheriated method
helps avoid redundant code by leveraging inherated methods

overloading:
Not supported in python

Super()
keyword used to call method from superclass

Abstract Class:
Contain one or more abstract methods: (identified by @abstractmethod decorator)
need to import ABC module
Abstraction is way of hiding the information

"""