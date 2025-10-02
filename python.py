'''
vowels = ("a", "e", "i", "o", "u")
text = input("Enter a line of text")

book = input("Type in a title of a book: ")
print("The length of the title is",len(book))
print("The books title is",str.upper(book))
'''

# Ask which file to read
filename = input("Enter file name (story.txt or news.txt): ")

# Open the file and read its contents
with open(filename, "r") as file:
    text = file.read().lower()

#the two dictionaries
letter_dict = {}
word_dict = {}

#count letters
for chr in text:
    if chr.isalpha():   #only letters
        if chr in letter_dict:
            letter_dict[chr] += 1
        else:
            letter_dict[chr] = 1

#Count words
words = text.split()
for word in words:
    word = word.strip(".,!?;:\"'()[]") #stip all punctuatioin out
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

#Print results.
print("The amount of letters is: ", letter_dict)
print("The amount of words are: ", word_dict)


