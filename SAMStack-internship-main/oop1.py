'''class student:
    pass
student1=student()
print("oop done" )'''

#task:
class student:
    def info(self,name,subject):
        self.name=name
        self.subject=subject
    def display(self):
        print("name=",self.name)
        print("subject",self.subject)
student1=student()
student2=student()
student1.info("Ahmed","oop")
student2.info("ali","calculus")
student1.display()
student2.display()

#bankaccount:
class bankaccount:
    def info(self,name,balance):
            self.name=name
            self.balance=balance
    def deposit(self,amount):
         self.balance+=amount
    def withdraw(self,amount):
         self.balance-=amount
    def display(self):
         print("account holder=",self.name)
         print("balance=",self.balance)
account_holder=bankaccount()
account_holder.info("inha",6000)
account_holder.deposit(4000)
account_holder.withdraw(1000)
account_holder.display()