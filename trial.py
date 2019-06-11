import numpy as np
import random
from dist_bw_pts import distance,new_point,border,coord_plot,start_point
import matplotlib.pyplot as plt
import time

start = time.time()
##d = int(raw_input("Enter the diameter of the fibre (in microns): "))
d = 6
A_f = np.pi * d**2 /4
##a = int(raw_input("Side of the square area to be filled: "))
a = 50
A = a**2

##V_f = float(raw_input("Preferred Volume fraction: "))
V_f = 0.13
n = int(V_f * A/A_f)
print n

border = border(a)

mag = 3*d/2
coord = [start_point(border, d)]
np_count = 0
for i in range(n-1):
    k = 1
    while (k > 0):
        np = new_point(random.randint(mag,(a-d)), coord[i])
        np_count += 1
        if (-a/2) <= np[0] <= (a/2) and (-a/2) <= np[1] <= (a/2):
            for l in range(len(border)):
                if distance(np,border[l]) < d:
                    break
            else:
                for j in range(i):
                    if distance(np,coord[j]) < mag:
                        break
                else:
                    break
            continue
        else:
            continue
               
    coord.append(np)
    
print coord
end = time.time()
print(end-start)


##coord_plot(border)
coord_plot(coord)
