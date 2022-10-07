

#Thinlayer_main1.py
#2022/10/7

import numpy as np
import matplotlib.pyplot as plt

import Thinlayer_def


startwl = 1.520 # [um]
stepwl = 0.0005 # [um]

nn = 100 # number of sampling point

# 1550nm * 0.25 --> 387.5 nm
# 387.5nm/1.463 --> 264.866 nm
# 387.5nm/2.130 --> 181.924 nm

  
L1 = [0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866]
L2 = [0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924]
 
mm = len(L1)

print('Length of L1 = ')
print(mm)

#print('L1 = ')

#        for aa in range(mm):        
#        print(L1[aa])
#        print('')


#print('L2 = ')

#        for bb in range(mm):          
#        print(L2[bb])
#        print('')


no = 1.000


wlcol = np.zeros(nn)
TPcol = np.zeros(nn)




for ii in range(nn):
    
    wl = startwl + stepwl*ii

    n1 = 1.463 + 0.003827/(wl**2) + 0.000/(wl**4)
    n2 = 2.1305 + 0.018499/(wl**2) + 0.00199850/(wl**4)
    ns = 1.6553 + 0.0086444/(wl**2) + 0.00081178/(wl**4)
    
    wlcol[ii] = wl
    Ein = np.array([[1],[0]])

    for jj in range(mm):

        th1 = L1[jj]
        th2 = L2[jj]           

        E_intermedate = Thinlayer_def.dielectric(wl, n1, n2, th1, th2, Ein)
        Ein = E_intermedate
            
    TP1 = abs(E_intermedate[0,0])**2
            
    TPcol[ii] = TP1

print('Wavelength = ')
print(wlcol)

print('Power = ')
print(TPcol)



#fig1 = figure(1)
#set(fig1,'Position',[10 200 300 300])
#plot(wlcol,10*log10(outputPcol),'r-');grid on;
