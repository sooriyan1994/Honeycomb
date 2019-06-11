import math
import random
import matplotlib.pyplot as plt

def distance(X1,Y1):
    if isinstance(X1,list) and isinstance(Y1, list):
        dis = math.sqrt((X1[0]-Y1[0])**2+(X1[1]-Y1[1])**2)
    else:
        print('ERROR. The inputs have to be of type "list"')
    return round(dis,4)

def new_point(mag, cp):
    n1 = round(random.uniform(-1,1),4)
    n2 = round(math.sqrt(1 - n1**2),4)
    if random.randint(0,1) == 0:
        x = cp[0] + (mag*n1)
        y = cp[1] + (mag*n2)
    else:
        x = cp[0] + (mag*n2)
        y = cp[1] + (mag*n1)
    np = [round(x,4),round(y,4)]
    return np

def border(sq_side):
    border = []
    deviation = [x * 0.1 for x in range(-sq_side*5,sq_side*5+1)]
    
    for i in range(4):
        for j in range(len(deviation)):
            if i%2 == 0:
                border.append([(-1)**(i/2) * (sq_side/2), (-1)**(i+i/2) * deviation[j]])
            else:
                border.append([(-1)**(i+i/2) * deviation[j], (-1)**(i/2) * (sq_side/2)])

    return border
            
def coord_plot(coord):
    X = []; Y = [];
    for i in range(len(coord)):
        X = X + [coord[i][0]]
        Y = Y + [coord[i][1]]
    plt.scatter(X,Y)
    plt.show()

def start_point(border, d):
    cp = border[random.randint(0, len(border)-1)]
    print cp
    return new_point(d, cp)
