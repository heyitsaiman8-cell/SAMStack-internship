# task 1:Dictionary operations
'''students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 8,
    "Fatima": 90
}
for name,marks in students.items():
    print(f"{name}: {marks} (Pass)") if marks>=60 else print(f"{name}: {marks} (Fail)")
print("Ali's marks:",students.get("Ali"))
print("students:",students.keys()  )
print("students:",students.values()  )'''

#task 2: set operations
'''student1={"python","java","c++","html"}
student2={"python","java","c#","css"}
print("student1:",student1)
print("student2:",student2)
print("the same subjects that they both study:",student1&student2)
print("the subjects that student1 study but student2 doesn't:",student1-student2)
print("the subjects that student2 study but student1 doesn't:",student2-student1)
print("the subjects that either student1 or student2 study:",student1|student2)'''

#task 3:word frequency analyzer
paragraph="python is a computer programming language.computer programming is fun and python is easy to learn"
words=paragraph.split()
word_frequency={}
for word in words:
    if word in word_frequency:
        word_frequency[word]+=1
    else:
        word_frequency[word]=1
print("repeated words:")
for word, frequency in word_frequency.items():
    if frequency > 1:
        print(f"{word}: {frequency}")
print("non-repeated words:")
for word, frequency in word_frequency.items():
    if frequency == 1:
        print(f"{word}: {frequency}")
print("all words:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
