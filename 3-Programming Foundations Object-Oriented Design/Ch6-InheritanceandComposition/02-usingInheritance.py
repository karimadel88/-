# class spaceship:
#     def setShield():
#         pass

# # that inherte from parent class (spaceShip)


# class CargoShuttle(spaceship):
#     pass
# #    super().setShield()


# what is Overriding ==> Alowing a subclass to replace the implementaion of a method from the superclass
# super.setShield()

# Python program to demonstrate
# calling the parent's class method
# inside the overridden method


class Parent():

    def show(self):
        print("Inside Parent")


class Child(Parent):

    def show(self):

        # Calling the parent's class
        # method
        super.show(self)
        print("Inside Child")


# Driver's code
obj = Child()
obj.show()
