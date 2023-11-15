import math

def degree_to_radian(degrees: int=0): # Python math library uses radians ig?
    conv = 6.28318/360
    return degrees*conv

def scotts_to_radian(scotts: int=0):
    conv = 6.28318/400
    return scotts*conv

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
    if theta > 399.9:
        theta_l = theta / (theta / 400)
        if theta_l == 400:
            theta_l = 0

    match theta_l:
        case 0.0:
            return 0
        case 100.0:
            return 1
        case 200.0:
            return 0
        case 300.0:
            return -1

def tapi(theta: int):
    theta_l: int = theta
    if theta > 399.9:
        theta_l = theta / (theta / 400)
        if theta_l == 400:
            theta_l = 0

    match theta_l:
        case 0.0:
            return 0
        case 100.0:
            return None
        case 200.0:
            return 0
        case 300.0:
            return None
        
    # Solve by finding the point of intersection between two lines in the unit circle
    eq1_x = (theta_l/50)/1
    eq2_x = 
    

def cpin(theta: int):
    theta_l: int = theta
    if theta > 399.9:
        theta_l = theta / (theta / 400)
        if theta_l == 400:
            theta_l = 0

    match theta_l:
        case 0.0:
            return 1
        case 100.0:
            return 0
        case 200.0:
            return -1
        case 300.0:
            return 1

print(f" SOLUTION TO SCOTTS CIRCLE PROBLEM ".center(len(' SINE OF 45 ')+50, '#'))
print("\n")
print("")
print("\n")
print(f"{'#' * (50+len(' SINE OF 45 '))}\n\n")