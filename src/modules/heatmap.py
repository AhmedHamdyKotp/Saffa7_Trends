
import cv2
import matplotlib.pyplot as plt
import sys
import numpy as np
sys.path.append('algorithms')
import hmap as k

X = []
Y = []
def getter (x,y) :
    for i in x :
        X.append(i)
    for i in y :
        Y.append(i)

def start (x , y):
    x_mesh, y_mesh ,xc= k.mesh(X, Y)
    intensity_l = k.distance(xc,X)
    inten = np.array(intensity_l)
    plt.pcolormesh(x_mesh,y_mesh,inten)
    plt.plot(x,y,'ro')
    plt.colorbar()
    plt.show()

    
