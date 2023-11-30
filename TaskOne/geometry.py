from math import pi as PI

def circleArea(radius: float) -> float:
    return radius**2 * PI

def triangleArea(base: float, height: float):
    return height * base / 2

def rectangleArea(sideA: float, sideB: float):
    return sideA * sideB