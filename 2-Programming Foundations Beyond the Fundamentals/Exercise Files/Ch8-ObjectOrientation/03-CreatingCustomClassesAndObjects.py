class Attendee:
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def getAttendee(self):
        print('name : {}, tickets : {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))


a1 = Attendee("karim", 1)
a2 = Attendee("eid", 2)

a1.getAttendee()
a1.addTicket()
a1.getAttendee()
