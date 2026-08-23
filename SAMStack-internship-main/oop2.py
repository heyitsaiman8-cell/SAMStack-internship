#public,private and protected data
class student:
    def info(self,name,age,email):
        self.name="eiman"
        self._age=20
        self.__email="xyz"
    def display(self):
        print("name=",self.name)
        print("age=",self._age)
        print("email=",self.__email)
student=student()
student.info("data",5,"email data")
student.display()

#getter and setter
print("============================================")
print("============getter and setter============")
print("============================================")
class student:
    def __init__(self,name,age):
        self._name="eiman"
        self.__age=20
    def get_name(self):
        return self._name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self._name=name
    def set_age(self,age):
        self.__age=age
student=student("eiman",20)
print(student.get_name())
print(student.get_age())
student.set_name("irha")
student.set_age("22")
print(student.get_name())
print(student.get_age())

# protect sensitive variables
print("============================================")
print("======protect sensitive variables=======")
print("============================================")
class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def show_balance(self):
        print("balance",self.__balance)
account=bankaccount(300000)
account.show_balance()