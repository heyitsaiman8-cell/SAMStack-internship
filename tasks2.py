'''#task 1:
text=input("enter a paragraph: ")
text=text.lower()
words=text.split()
text=text.replace(".","")
text=text.replace(",","")
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
        print("\nword frequency:")
for word,count in word_count.items():
    print(word,":",count)'''

 #task 2:
'''try:
    with open("grades.txt", "r") as file:
        total = 0
        count = 0

        for line in file:
            name, score = line.strip().split(",")
            total += int(score)
            count += 1

        average = total / count
        print("Average score:", average)

except FileNotFoundError:
    print("File not found. Please make sure 'grades.txt' exists in the current directory.")'''

#task 3:
numbers=[12,45,67,89,23,56,78,90,34,21]
filtered_numbers=[number for number in numbers if number>15 and number%3==0]
print("Original numbers:", numbers)
print("Filtered numbers:", filtered_numbers)