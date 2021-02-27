class Person:

    def __init__(self, name):
        self.name = name

        self.charges_list = []

    def addCharge(self, charge):
        self.charges_list.append(charge)
