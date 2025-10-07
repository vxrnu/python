import math 
numbers = int(input("How many numbers do you want to enter: ")) #asking how many numbers

number = []
floor = []
ceil = []
trunc = []

for x in range(numbers):
    num = float(input(f"Enter number {x+1}: "))
    number.append(num)
    floor.append(math.floor(num))
    ceil.append(math.ceil(num))
    trunc.append(math.trunc(num))

print(number, floor, ceil, trunc)

