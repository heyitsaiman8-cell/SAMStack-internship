# task 1: dynamic typing and input function
'''Name=input("Enter your name: ")
Semester=input("Enter your semester: ")
CGPA=input("Enter your CGPA: ")
print(f"Hello {Name}, I am in semester {Semester} and my CGPA is {CGPA}. ")
Semester=int(input("Enter your semester:    "))
CGPA=float(input("enter your cgpa: "))
print(type(Name))
print(type(Semester))
print(type(CGPA))'''

# task 2:control flow and lists
'''import random
numbers=[1,12,5,8,22,3,7,9,15,100]
even_numbers=[]
odd_numbers=[]
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
'''

#task 3:functions and loops
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
num=int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")  
else:
    print(f"{num} is not a prime number.")
