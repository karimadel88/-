# linked list is linear collection of data, elemant,called node
# contain refernce to the next node in the list
# hold whetever data the application needs
# 2,r->3,r->4,r->null
# linked list can add or remove from first or end in big o(1)
# no random access

# linked list implemmition


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self, next):
        self.next = next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=Node):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        newNode = Node(data)
        newNode.set_next(self.head)
        self.head = newNode
        self.count += 1
