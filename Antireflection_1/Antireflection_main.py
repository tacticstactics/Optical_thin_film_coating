#Antireflection_main.py

import math
from tkinter import NS
import numpy as np
import matplotlib.pyplot as plt

import Antireflection_def


 # thin_AR_func.m
 # L -> 0;	H ->	1;

 #function [wlcol,dBTcol,dBRcol] = ...
 #   thin_AR_func(startwl,stepwl,centerwl,mm,layer,thkpara); 
 #global c;

startwl = 1.200 # [um]
stepwl = 0.002 # [um]

mm = 512 # number of sampling point

layer1 = np.array([1, 2, 1, 2])

thkpara = np.array([0.181924, 0.181924, 0.181924, 0.181924])

len_layer1 = len(layer1)
print('Length of L1 = ')
print(len_layer1)

wlcol= np.zeros(mm,1)
P1dBcol=np.zeros(mm,1)
P2dBcol=np.zeros(mm,1)
 

for ii in range(mm):   

    wl = startwl + stepwl *ii
    wlcol[ii,1] = wl

    TMin = np.array([[1,0],[0,1]])
    
    n0 = 1
    ns = 1.463 + 0.003827/(wl**2) + 0.000/(wl**4)
    

    for kk in range(len_layer1):

        n_index = layer1[kk]
        thickness1 = thkpara[kk]

        TM_intermediate = Antireflection_def.transfermatrix(wl, n_index, thickness1, TMin)

        TMin = TM_intermediate
        #inner loop ended
        
    TMout = TM_intermediate

    print(TMout)

    #     m11 = TMout[0,0]
    #     m12 = TMout[0,1]
    #     m21 = TMout[1,0]
    #     m22 = TMout[1,1]

     


       #B = m11 + m12*ns
       #C = m21 + m22 * ns
       
       #er = (n0*B - C) / (n0 * B + C)     
       #et = (2*n0) / ((m11 + m12*ns)*n0 + (m21 + m22*ns))
       
       er = 1
       et = 0

       Pow1 = np.abs(er)**2
       Pow2 = np.abs(et)**2 * ns/n0
       
       P1dBcol[ii] = -10*np.log(Pow1)
       P2dBcol[ii] = 10*np.log(Pow2)

    #outer loop ended


fig = plt.figure(figsize = (8,4), facecolor='lightblue')
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(wlcol,P1dBcol)
ax1.set_xlabel("Wavelength")
ax1.set_ylabel("Power")
ax1.grid()

ax2.plot(wlcol,P2dBcol)
ax2.grid()
ax2.set_xlabel("Wavelength")

plt.show()