# python can't differ between public and private
# and we use __ __ to deal as private
# and that because Python is dynamic language


class SpaceShip():
    def __init__(self) -> None:
        # instanse variables (attribute)
        self.callSign = ''
        self.shieldStrength = 100

    # methods (behavior)
    def fireMissile(self):
        return "Pew!"

    def reduceShield(self, amount):
        self.shieldStrength -= amount

# when create object we create digram and we can creat also classes from main object by use new keyword in most language
# in python cant need new keyword


myShip = SpaceShip()
myShip.callSign = "Excelsior"
myShip.shieldStrength(100)

# Constructor ==> A special method that gets called to create object
