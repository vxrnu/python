import math
def rug_calculator(radius):
    radius = float(input("Enter the radius of the rug in metres: "))
    circumference = 2 * math.pi * radius
    circumference.ceil()
    area = math.pi * radius ** 2
    area.ceil()
    