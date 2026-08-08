#task 1:
'''sentence=input("Enter a sentence: ")
unique_characters=set(sentence)
print("Unique characters in the sentence:", unique_characters)
print("total unique characters:", len(unique_characters))'''

#task 2:
'''text="Python is a high-level, interpreted programming language"
text=text.lower()
text=text.replace(".","")
text=text.replace(",","")   
text=text.replace("'","")
text=text.replace("!","")
words=text.split()
word_frequency={}
for word in words:
    if word in word_frequency:
        word_frequency[word]+=1
    else:
        word_frequency[word]=1
        print("word frequency:",word_frequency)'''

#task 3:
def is_palindrome(word):
    left=0
    right=len(word)-1
    while left<right:
        if word[left]!=word[right]:
            return False
        left+=1
        right-=1
    return True
word=input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")   