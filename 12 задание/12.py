class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_name(self):
        print(self.name)
    def get_salary(self):
        print(self.salary)
    def increase_salary(self):
        self.salary *= 1.1
emp = Employee("Евгений", 50000)
emp.get_name()
emp.get_salary()
emp.increase_salary()
emp.get_salary()