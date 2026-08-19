# inheritance and polymorphism
# task 1:single inheritance
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Intern(Employee):
    def __init__(self, name, duration):
        super().__init__(name)
        self.duration = duration

    def show(self):
        self.display()
        print("Duration:", self.duration, "months")


student = Intern("Eiman", 3)
student.show()

# multiple inheritance
print("===============================")
print("===== multiple inheritance====")
print("===============================")
class employee:
    def info1(self):
        print("name=ali")
class developer:
    def info(self):
        print("skill=python")
class intern(employee,developer):
    def show(self):
        self.info1()
        self.info()
        print("status=intern")
student=intern()
student.show()

# task 2:override
print("===============================")
print("========== override==========")
print("===============================")
class employee:
    def work(self):
        print("employee is working")
class intern(employee):
    def work(self):
        print("intern is learning")
employe=employee()
interns=intern()
employe.work()
interns.work()

#task 3 base class and derived class concept
print("=====================================")
print("base class and derived class concept")
print("=====================================")
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
class fulltimeemploy(Employee):
     def display(self):
            print("fulltimeemployee Name:", self.name)
class intern(Employee):
     def display(self):
            print("intern Name:", self.name)
student=fulltimeemploy("urhan")
students=intern("irhan")
student.display()
students.display()
    