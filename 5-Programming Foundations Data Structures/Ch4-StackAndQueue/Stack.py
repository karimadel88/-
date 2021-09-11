class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()


deack = Stack()
deack.add("Heart : Queen")
deack.add("Spade : Jack")
deack.add("Heart : 9")
deack.add("Diomand : 4")

print(deack.remove())
