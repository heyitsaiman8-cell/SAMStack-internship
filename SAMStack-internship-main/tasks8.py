'''# modules:
import math
number=int(input("Enter a number: "))
print("Square root of", number, "is", math.sqrt(number))
print("Factorial of", number, "is", math.factorial(number))
print("Square of", number, "is", pow(number, 2))
print("The value of pi is:", math.pi)
print("The value of e is:", math.e)
print("math.ceil(9.2) is:", math.ceil(9.2))
print("math.floor(5.8) is:", math.floor(5.8))

import datetime
now = datetime.datetime.now()
print("Current date and time:", now)
time=datetime.datetime.now().time()
print("Current time:", time)
date=datetime.datetime.now() + datetime.timedelta(days=1)
print("Tomorrow's date:", date)

import random
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

import turtle
t = turtle.Turtle()
t.circle(100)
turtle.done()
'''

'''#json.load() and json.dump()
import json
data = '{"name": "Ali", "age": 25, "city": "Karachi"}'
info = json.loads(data)
print(info)
print(info["name"])

students = { "name": "Ali", "age": 25, "city": "Karachi" }
informations=json.dumps(students)
print(informations)
'''

#json configuration manager
import json
config = { "app-name": "MyApp", "version": "1.0", "author": "Ali" }
with open("config.json", "w") as file:
    json.dump(config, file,indent=4)
    print("Configuration saved to config.json.")

with open("config.json", "r") as file:
 config_data = json.load(file)
print("Configuration loaded from config.json:")
print(config_data)
print("App Name:", config_data["app-name"])
print("version:",config_data["version"])
print("author:",config_data["author"])
config_data["author"]="eiman"
config_data["version"]="3.0"

json_string=json.dumps(config_data,indent=4)
print("updated json:")
print(json_string)
information=json.loads(json_string)
print("python dictionary")
print(information)
with open("config.json","w") as file:
 json.dump(config_data,file,indent=4)
 print("successfully updation done")