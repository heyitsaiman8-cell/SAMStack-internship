'''# task 1: list operations
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
print("third element:", numbers[2])
print("first 3 elements:", numbers[0:3])
numbers.append(60)
print("List after appending 60:", numbers)
numbers.remove(20)
print("List after removing 20:", numbers)
numbers.insert(2, 25)
print("List after inserting 25 at index 2:", numbers)
removed_element = numbers.pop(3)
print("Removed element at index 3:", removed_element)
print("final list:", numbers)'''

# task 2: tuple,immutablility,packing and unpacking
'''student_info = ("eiman", 20, "Computer Science")
print("Original tuple:", student_info)
print("Name:", student_info[0])
print("Age:", student_info[1])
name, age, major = student_info
print("Unpacked values - Name:", name, ", Age:", age, ", Major:", major)'''

#task 3: list comprehension,map,filter and reduce
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
even_numbers=[x for x in numbers if x % 2 == 0]
print("Original list:", numbers)
print("Squared numbers:", squared_numbers)
print("Even numbers:", even_numbers)