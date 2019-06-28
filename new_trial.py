import numpy
#from dist_bw_pts import distance,coord_plot
#import matplotlib.pyplot as plt
import time
import math

start = time.time()
##d = int(raw_input("Enter the diameter of the fibre (in microns): "))
d = 6
A_f = numpy.pi * d**2 /4
##a = int(raw_input("Side of the square area to be filled: "))
a = 60
A = a**2

dis = 0.1 #Distance betweeen two fibers
mag = d + dis # Minimum Distance between two fiber centers

#A_f_act = numpy.pi * (mag)**2 / 4
#A_act = (a-2*d)**2
#n_max = A_act/A_f_act
#V_f_max = float(int(n_max) * A_f / A)
#print n_max

##V_f = float(raw_input("Preferred Volume fraction: "))
V_f = 0.4

n = int(V_f * A/A_f)
#n = 50
#V_f = round(A_f * n/A,3)
#print ' Volume fraction : ',V_f
print('Number of fibers to be filled in the area : ', n)

dist_border = 0.1 # from the edge and the edge of fiber

x = numpy.linspace(dist_border+d/2, a-(dist_border+d/2), 500, dtype=numpy.float)
y = numpy.linspace(dist_border+d/2, a-(dist_border+d/2), 500, dtype=numpy.float)

space = numpy.stack(numpy.meshgrid(x, y), -1).reshape(-1,2)

for i in range(n):
        print(len(space))
        np = space[numpy.random.randint(len(space))]
        coord.append(np)
        temp = []
##        temp = list(space)
##        
        for l in range(len(space)):
                if math.sqrt((space[l][0]-np[0])**2+(space[l][1]-np[1])**2) < mag:
                        temp.append(l)
##
        ##space = list(temp[m])
        space = numpy.delete(space, temp, axis = 0)
##        
##                
##print(coord)
end = time.time()
print(end-start)

##coord_plot(border)
#coord_plot(coord)

# plot
#plt.figure(figsize=(10*width_ratio,10))
#plt.scatter(coord[:,0], coord[:,1], s=3)
#plt.show()
