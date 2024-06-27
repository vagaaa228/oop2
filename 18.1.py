class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self):
        pass

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def setAge(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            raise Exception('Incorrect')


arthur = Employee()
arthur.setName('Arthur')
arthur.setSalary(3600)
arthur.setAge(25)

print(arthur.getName())
print(arthur.getSalary())
print(arthur.getAge())
