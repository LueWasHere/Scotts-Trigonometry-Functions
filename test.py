import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import symbols, solve, sqrt

def make_values():
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

    li_ls = []

    for value_d in range(0, 400):
        li_ls.append(sipi((value_d)))

    li_ls = np.array(li_ls)

    print(li_ls)

    return li_ls

# Generate x values
x_values = np.linspace(-1, 1, 400)

# Calculate y values for upper and lower halves
y = make_values()

# Plot the unit circle
plt.figure(figsize=(6, 6))
plt.plot(x_values, y, label='Sipi Function')

# Set axis limits and labels
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Sipi Function')
plt.xlabel('x')
plt.ylabel('y')

# Add legend
plt.legend()

plt.savefig('unit_circle_plot_scotts.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()