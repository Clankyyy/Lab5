from math_operations import add, multiply, divide, subtract
from temperature_conversion import fahrToCell, celToFahr
from validation import isEven
from geometry import circleArea, triangleArea, rectangleArea

if __name__ == "__main__":

    print("task 1")
    a, b = 1, 2
    print("a = {0}, b = {1}".format(a, b))
    print("a + b = ", add(a, b))
    print("a * b = ", multiply(a, b))
    print("a - b = ", subtract(a, b))
    print("b / a = ", divide(b, a))

    print("\ntask 2")
    testVal1 = 0
    testVal2 = 32
    testVal3 = 100

    print("{0} celsius to fahrenheit - {1}".format(testVal1, celToFahr(testVal1)))
    print("{0} celsius to fahrenheit - {1}".format(testVal2, celToFahr(testVal2)))
    print("{0} fahrenheit to celsius - {1}".format(testVal1, fahrToCell(testVal1)))
    print("{0} fahrenheit to celsius - {1}".format(testVal3, fahrToCell(testVal3)))

    print("\n task 3")

    print("Enter number")
    num = int(input())

    if isEven(num):
        print("Number {0} is even".format(num))
    else: 
        print("Number {0} is odd".format(num))
    
    print("\ntask 4")

    radius = 3

    base = 10
    height = 5

    sideA = 10
    sideB = 2
    print("Area of circle with radius {0} is {1}".format(radius, circleArea(radius)))   
    print("Area of triangle with base {0} and height {1} is {2}".format(base, height, triangleArea(base, height)))
    print("Area of rectangle with sides {0} and  {1} is {2}".format(sideA, sideB, rectangleArea(sideB, sideA)))