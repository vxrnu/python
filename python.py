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


vowels = ("a", "e", "i", "o", "u")
text = input("Enter a line of text: ")
for chr in text:
    if vowels == chr