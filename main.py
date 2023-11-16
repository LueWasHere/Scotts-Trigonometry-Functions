import math
from sympy import symbols, solve, sqrt

def degree_to_radian(degrees: int=0): # Python math library uses radians ig?
    conv = 6.28318/360
    return degrees*conv

def scotts_to_radian(scotts: int=0):
    conv = 6.28318/400
    return scotts*conv

def degree_to_scotts(degree: int=0):
    conv = 360/400
    return degree*conv

print(" SINE OF 45 ".center(len(" SINE OF 45 ")+50, '#'), end='\n\n')
print(math.sin(degree_to_radian(45)))
print(20*math.sin(degree_to_radian(45))) # Observe
print(f"\nThe python math library uses radians instead of degrees, \nso sin({degree_to_radian(45)}) == 0.7071 instead of sin(45) == 0.7071")
print(f"\n{'#' * (50+len(' SINE OF 45 '))}\n\n")
print(f" PROOF OF CONCEPT ".center(len(' SINE OF 45 ')+50, '#'))
print("\nBased on this, it's actually fairly simple to make a \ncalculator that uses scotts instead of radians or degrees")
print(f"\nUsing the conversion factor {6.28318/400} we can\nconvert scotts to radians and plug them directly into the\nfunction.\n")
print(f"\nsin(50) == {math.sin(scotts_to_radian(50))}\ntan(50) == {math.tan(scotts_to_radian(50))}\ncos(50) == {scotts_to_radian(50)}\n")
print(f"{'#' * (50+len(' SINE OF 45 '))}\n\n")

def sipi(theta: int):
    theta_l: int = theta
    # Check for a negative angle
    if theta < 0:
        theta_l += 400 * math.floor(theta_l / 400)
    # Check for an angle that is greater than or equal to 400 scotts
    if theta_l >= 400:
        theta_l = theta_l / math.floor(theta_l / 400)
    if (theta_l % 400) == 0 or theta_l == 0.0:
        return 0
    
    theta_a = theta_l
    if theta_l > 100:
        theta_l -= 100
    elif theta_l < 100:
        theta_l = (100-theta_l)
    elif theta_l == 100:
        return 1
    if theta_l >= 100:
        theta_l -= 100
        if theta_l > 100:
            theta_l -= 100
        elif theta_l < 100:
            theta_l = (100-theta_l)
        elif theta_l == 100:
            return -1
    

    try:
        theta_l = theta_l/(200-(100+theta_l))
    except ZeroDivisionError:
        return 0

    x = symbols('x')

    if theta_a <= 200:
        un_cu = sqrt(1 - x**2)
    else:
        un_cu = -(sqrt(1 - x**2))

    sin_v = theta_l * x

    # Solve for the intersection point
    intersection = solve(sin_v - un_cu, x)[0]

    return intersection

def tapi(theta: int):
    theta_l: int = theta
    if theta_l >= 400:
        theta_l = theta / (theta / 400)
        if theta_l == 400:
            theta_l = 0

    

def cpin(theta: int):
    theta_l: int = theta
    if theta_l >= 400:
        theta_l = theta / (theta / 400)
    if (theta_l % 400) == 0 or theta_l == 0.0:
        theta_l = 1

    v = sipi(theta_l)
    if (theta_l >= 0 and theta_l <= 100) or (theta_l >= 300 and theta_l <= 400):
        return math.sqrt(1-v**2)
    else:
        return -(math.sqrt(1-v**2))

print(f" SOLUTION TO SCOTTS CIRCLE PROBLEM ".center(len(' SINE OF 45 ')+50, '#'))
print("\n")
print("")
print("\n")
print(f"{'#' * (50+len(' SINE OF 45 '))}\n\n")

print(sipi(200))
print(degree_to_radian(28))