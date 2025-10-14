'''
WEEK 03 Exercise - Application of recent learning
Incorporate your recent studies of Python data structures and file handling to solve the following, e.g. 
- file handling and methods
- strings
- lists
- sets and/or dictionaries

along with the relevant functions/methods they offer.

Paul Knighton
'''
# Open a word_list.txt file for reading
with open("words.txt", "r") as file:
# Main file reading loop:
    lines = []
    for line in file:
        lines.append(line.strip())
# read all lines into a list 
# count the number of lines in a file
number=len(lines)

# Main processing of list:
# print all items in the list
# print the number of items in the list

# print all items in the list in alphabetic order A-Z (ascending), e.g. sorted.
ascending_lines = sorted(lines)
print(ascending_lines)

# print all items in the list in alphabetic order Z-A (descending), eg sorted and reversed.
descending_lines = sorted(lines, reverse=True)
print(descending_lines)

# print the shortest word and its' length
shortest_word = min(lines, key=len)
print(f"The shortest word is {shortest_word} with a length of {len(shortest_word)}")

# print the longest word and its' length
longest_word = max(lines, key=len)
print(f"The longest word is {longest_word} and the length of the word is {len(longest_word)}")


# print number of items in the list, the first item and the last item of list.
print(lines[0])
print(lines[number - 1])

# print only the unique items in the list, along with the number of times each one occurs in the list
# print the number of unique items in the list
with open("words.txt", "r") as file:
    lines = file.read().split()

for i in lines:
    if i[0].isupper():
        print(i)

# Scrabble / Word finder v1:
# in a loop ask the user for a start letter,
# then print all words beginning with a specific letter, which the user inputs.
# e.g. "a"
# andes
# apple
# avalanche

# Scrabble / Word finder v2:
# Extend your Scrabble / Word finder to print all words beginning with a specific letter, which are a specific number of letters long, which the user inputs.
# e.g. inputs of "e" and "6" would find.
# echoes