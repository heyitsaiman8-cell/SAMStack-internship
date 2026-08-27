import pandas as pd
print("============================")
print("======group by========")
print("============================")
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Department": ["CS", "IT", "CS", "IT", "CS"],
    "Marks": [80, 75, 90, 85, 70]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())

print("\nTotal Marks by Department:")
print(df.groupby("Department")["Marks"].sum())

print("\nStudents Count by Department:")
print(df.groupby("Department")["Name"].count())

print("============================")
print("======.agg========")
print("============================")
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Department": ["CS", "IT", "CS", "IT", "CS"],
    "Marks": [80, 75, 90, 85, 70]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Marks"].agg(["mean","sum","count"])

print(result)

print("============================")
print(".merge() Inner, Left, Right")
print("============================")
students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3, 5],
    "Marks": [80, 75, 90, 88]
})

print("Students:")
print(students)

print("\nMarks:")
print(marks)

print("\nINNER JOIN:")
print(pd.merge(students, marks, on="Student_ID", how="inner"))

print("\nLEFT JOIN:")
print(pd.merge(students, marks, on="Student_ID", how="left"))

print("\nRIGHT JOIN:")
print(pd.merge(students, marks, on="Student_ID", how="right"))