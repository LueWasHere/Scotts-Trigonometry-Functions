import math

def scotts_to_radian(x):
    conv = 6.28318/400
    return x*conv

str_l = ""
for i in range(0, 400):
    str_l += f"{i}, {math.sin(scotts_to_radian(i))}\n"

with open("dat_file.txt", 'a') as f:
    f.write(str_l)
    f.close()