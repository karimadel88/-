# instance Variables => Variables for which each instantiated object of a calss has a separate copy
# Static Variables (a shared variable) => Variable that is shared across all objects in a class
# Can do that in python by declare variable out of init method or constructor


class Spaceship():
    # Static Var.
    toughness = 0.8
    # instans Var.

    def __init__(self) -> None:
        pass
        # what declare here is instanse Var.

# Creating Static Methods
    @staticmethod
    def fun():
        pass
