

#Thinlayer_main1.py
#2022/10/7
# Takeshi Ozeki, Optical Curcit. p.89 multilayer dielectric film filters

import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

import thinlayer_def


startwl = 1.200 # [um]
stepwl = 0.002 # [um]

nn = 512 # number of sampling point

# Asssume quarter waelength
# 1550nm * 0.25 --> 387.5 nm (Air)
# 387.5nm/1.463 --> 264.866 nm (nL)
# 387.5nm/2.130 --> 181.924 nm (nH)

  
L1 = [0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866]

L2 = [0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924]

 
mm = len(L1)

print('Length of L1 = ')
print(mm)


n0 = 1.000 #refractive Index of Air


wlcol = np.zeros(nn)
P1dBcol = np.zeros(nn)
P2dBcol = np.zeros(nn)
P1_phasecol = np.zeros(nn)
P2_phasecol = np.zeros(nn)

Ein = np.array([[1],[0]]) 

for ii in range(nn):   
    
   wl = startwl + stepwl*ii
   wlcol[ii] = wl
   #print(wl)

   n1 = 1.463 + 0.003827/(wl**2) + 0.000/(wl**4)
   n2 = 2.1305 + 0.018499/(wl**2) + 0.00199850/(wl**4)
   #ns = 1.6553 + 0.0086444/(wl**2) + 0.00081178/(wl**4)
   
   TM_eye = np.array([[1,0],[0,1]]) 

   D01 = np.array([[(n0+n1)/(2*np.sqrt(n0*n1)), (n1-n0)/(2*np.sqrt(n0*n1))],[(n1-n0)/(2*np.sqrt(n0*n1)), (n0+n1)/(2*np.sqrt(n0*n1))]]);# Air to n1 material (typically SiO2)

   TMin = np.dot(D01, TM_eye)
   
   for jj in range(mm):

        #print(jj)

        th1 = L1[jj]
        th2 = L2[jj]           

        TM_intermedate = thinlayer_def.dielectric(wl, n1, n2, th1, th2, TMin)
        TMin = TM_intermedate
        #print(E_intermedate)
    
   TM_stack = TM_intermedate
    
   detTMout = np.linalg.det(TM_stack) # Verify det is unity.
   #print("det = ", detTMout)

   Eout1 = np.dot(TM_stack, Ein)

   T_substrate = np.array([[np.exp(-1j*n1*0.0001*2*math.pi/wl), 0], [0, np.exp(1j*n1*0.0001*2*math.pi/wl)]]);

   Eout2 = np.dot(T_substrate, Eout1)

   D10 = np.array([[(n1+n0)/(2*np.sqrt(n0*n1)), (n0-n1)/(2*np.sqrt(n0*n1))],[(n0-n1)/(2*np.sqrt(n0*n1)), (n1+n0)/(2*np.sqrt(n0*n1))]]);# n1 material (typically SiO2) to Air

   Eout3 = np.dot(D10, Eout2)


   Eout3_x = Eout3[0,0]   
   Eout3_y = Eout3[1,0]
   
   Pow1 = np.abs(Eout3_x)**2
   P1_Phase = cmath.phase(Eout3_x)
   P1_phasecol[ii] = P1_Phase



   coef1 = mm*2+2
   Pow2 = (n1/n2)**coef1 * np.abs(Eout3_y)**2  

   P2_Phase = cmath.phase(Eout3_y)
   P2_phasecol[ii] = P2_Phase


   P1dBcol[ii] = -10*np.log(Pow1)
   P2dBcol[ii] = 10*np.log(Pow2)


fig = plt.figure(figsize = (8,4), facecolor='lightblue')

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.plot(wlcol,P1dBcol)

ax1.set_xlabel("Wavelength")
ax1.set_ylabel("Power")
ax1.grid()

ax2.plot(wlcol,P1_phasecol)
ax2.set_ylabel("Phase")
ax2.grid()

ax3.plot(wlcol,P2dBcol)
ax3.grid()
ax3.set_xlabel("Wavelength")

ax4.plot(wlcol,P2_phasecol)
ax4.grid()

plt.show()

