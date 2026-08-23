'''# task 1: text file I/O
with open("data.txt", "w") as file:
    file.write("Hello, World!")
    print("Data written to file.")
    with open("data.txt", "r") as file:
        data=file.read()
        print("data can be read")
        with open("data.txt","a") as file:
            file.write("\nhere append mode is used")
            print("append mode done")
            with open("data.txt","r") as file:
             for line in file:
                print(line.strip())
'''

#task 2:csv
'''import csv
students = [["ali",20,"male"],["sara",30,"female"],["ahmed",25,"male"],["fatima",28,"female"]]
with open("data.csv", "w", newline="") as file:
    data = csv.writer(file)
    data.writerow(["Name", "Age", "Gender"])
    for student in students:
        data.writerow(student)

print("Data written to CSV file.")'''

#task 3:persistent data
name = input("Enter your name: ")
contact = input("Enter your contact number: ")
with open("information.txt", "a") as file:
    file.write(f"Name: {name}, Contact: {contact}\n")
    print("Data saved to file.")