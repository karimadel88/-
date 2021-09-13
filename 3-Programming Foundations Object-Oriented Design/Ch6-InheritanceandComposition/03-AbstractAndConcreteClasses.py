# Abstract class => Exists for other classes to inherit
# cannot be instantiated
# contains at least one abstract method

# example from geeks for geeks to explain that

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()  # I have 3 sides

K = Quadrilateral()
K.noofsides()  # I have 4 sides

R = Pentagon()
R.noofsides()  # I have 5 sides

K = Hexagon()
K.noofsides()  # I have 6 sides
