#Thinlayer_def.py
# Takeshi Ozeki, p.89 multilayer dielectric film filters

import numpy as np
import math


def dielectric(wl, n1, n2, th1, th2, Ein):

    T1 = np.array([[np.exp(-1j*n1*th1*2*math.pi/wl), 0], [0, np.exp(1j*n1*th1*2*math.pi/wl)]]);
    T2 = np.array([[np.exp(-1j*n2*th2*2*math.pi/wl), 0], [0, np.exp(1j*n2*th2*2*math.pi/wl)]]);


    D21 = (1/(2*np.sqrt(n1*n2)))* np.array([[n1+n2, n2-n1],[n2-n1, n1+n2]]);
    D12 = (1/(2*np.sqrt(n1*n2)))* np.array([[n1+n2, n1-n2],[n1-n2, n1+n2]]);

    #n2 > n1

    # T matrix

    E1 = np.dot(T1,Ein)
    E2 = np.dot(D21,E1)
    E3 = np.dot(T2,E2)
    E4 = np.dot(D12,E3)

    #Eout = E3 #        Eout = D12*T2*D21*Eini # each 
    
 
    Eout = E4

    return Eout
