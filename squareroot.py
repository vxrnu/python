import math
def is_square():
    n = -1
    while n != 0:
        n = int(input("Pick a number to square root:    "))
        root = math.sqrt(n)
        if root == int(root):
            print("True")
        else:
            print("False")
is_square()
