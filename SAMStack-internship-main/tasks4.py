'''# task 1:
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("error: Cannot divide by zero.")
    except ValueError:
        print("error: Please enter numeric values.")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    divide(num1, num2)
except ValueError:
    print("error: Please enter valid numbers.")'''


# task 2:
"""raw_data = "Name: Eiman | ID: 1024 | Status: Active | Email: abc"
parts = raw_data.split(" | ")
data = {}
for part in parts:
    key, value = part.split(": ", 1)
    data[key] = value
result = {
    "ID": data["ID"],
    "Email": data["Email"],
    "status": data["Status"]
}
print(result)"""

# task 3:
class InvalidSemesterError(Exception):
    pass
def check_semester():
    try:
        semester = int(input("Enter your semester (1-8): "))
        if semester < 1 or semester > 8:
            raise InvalidSemesterError(
                "Invalid semester: Please enter a value between 1 and 8."
            )
        print("Valid semester:", semester)
    except InvalidSemesterError as e:
        print("Error:", e)
    except ValueError:
        print("Error: Please enter a valid number.")
check_semester()