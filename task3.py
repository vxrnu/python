'''
#Task 1a
book = input("Type in a title of a book: ")
print("The length of the title is: ", len(book))
print("The books title is: ", str.upper(book))
'''

'''
# Task 1b
Coffee = int(input("How many coffees were sold today?"))
Tea = int(input("How many teas were sold today?"))
Teasold = Tea * 2
Coffeesold = Coffee * 3
Total = Teasold + Coffeesold
print(Total)
'''

'''
#Filename = input("Enter your text file")
filename = "Sales.txt"
with open(filename, "r") as file:
    content = file.read()
    lines = file.readlines()
    print(content)
print(lines)
print("The amount of character in the file are: ", len(content))
'''

'''
#task 2a
vowel = 0
constenants = 0
space = 0
vowels=("a", "e", "i", "o", "u")
text = input("Enter a line of text: ")
for chr in text.lower():
    if chr in vowels:
        vowel += 1
    elif chr.isalpha():
        constenants += 1
    elif chr.isspace():
        space += 1    
print(vowel)
print(constenants)
print(space)
'''

#text = input("Enter a line of text")
text = "abcdef ghijklm nopqrst uvwxyz eee"
text = text.lower()

vowel = 0
consonants = 0
space = 0
vowels=("a", "e", "i", "o", "u")

letters_dict = {}
words_dict = {}

for chr in text.lower():
    if chr in vowels:
        vowel += 1
        # if letter in dict, add one to count
        # else letter not in dict, so add for first time and make count 1.
        if chr in letters_dict:
            letters_dict[chr] += 1
        else:
            letters_dict[chr] = 1

    elif chr.isalpha(): #alphanumeric
        consonants += 1
        if chr in letters_dict:
            letters_dict[chr] += 1
        else:
            letters_dict[chr] = 1   

    newchr = text.strip().split()
    for newchr in text:
        if newchr in text:
            words_dict[newchr] +=1
        else:
            words_dict[newchr] =1
        

print(letters_dict)
print(words_dict)