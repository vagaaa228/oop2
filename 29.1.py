class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Employee(User):
    pass

art = Employee()
art.setName('Arthur')

print(art.getName())