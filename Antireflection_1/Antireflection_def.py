#Antireflection_def.py

import numpy as np
import math



def transfermatrix(wl, n_index, th1):

    nL = 1.463 + 0.003827/(wl**2) + 0.000/(wl**4)
    nH = 2.1305 + 0.018499/(wl**2) + 0.00199850/(wl**4)
    #nQuartz = 1.6553 + 0.0086444/(wl.^2) + 0.00081178./(wl.^4)
    #nLN = sqrt(2.23413 + ((2.68312-wl.^2)/(wl.^2-0.04481)) + ((2.59121.* wl)/(wl - 109.776)));
 
    #substrate: quartz
  
    match n_index:

        case 1:
            n_index = nL
        case 2:
            n_index = nH


    sigma = 2 * math.pi *n_index*th1/wl

   	#Mjj = np.array([[math.cos(sigma), ],[np.exp(1j*n1 * math.sin(sigma)), math.cos(sigma)]])
   	
    TM_intermedate = np.array([[math.cos(sigma),np.exp(1j)*math.sin(sigma)/n_index],[np.exp(1j)*math.sin(sigma)/n_index,math.cos(sigma)]])

    return TM_intermedate





