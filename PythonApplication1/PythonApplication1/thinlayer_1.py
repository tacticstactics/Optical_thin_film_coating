

#thinlayer_1.py
#2022/10/7

import numpy as np
import matplotlib.pyplot as plt


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
print('')


no = 1.000
input = np.array([[1],[0]])

wlcol = np.zeros(m)
Tcol = np.zeros(m)
outputPcol = np.zeros(m)

Eini = np.identity(2)


for ii in range(nn):
    
    wl = startwl + stepwl*ii
    n1 = 1.463 + 0.003827/(wl**2) + 0.000/(wl**4)
    n2 = 2.1305 + 0.018499/(wl**2) + 0.00199850/(wl**4)
    ns = 1.6553 + 0.0086444/(wl**2) + 0.00081178/(wl**4)
    
    wlcol[ii] = wl



for jj in range(mm):
        T1 = np.array([[np.exp(-1j*n1*L1[jj]*2*pi/wl) 0,],[0, np.exp(1j*n1*L1[jj]*2*pi/wl)]])
        T2 = np.array([[np.exp(-1j*n2*L2[jj]*2*pi/wl) 0],[0, exp(1j*n2*L2[jj]*2*pi/wl)]])

        D21 = (1/(2*np.sqrt(n1*n2))).* np.array([[n1+n2, n2-n1],[n2-n1, n1+n2]])
        D12 = (1/(2*np.sqrt(n1*n2))).* np.array([[n1+n2, n1-n2],[n1-n2, n1+n2]])      

        Eout1 = np.dot(D21,Eini)




        Eout = D12*T2*D21*Eini # each

        Pcol[jj] = abs(Eout[0,0])**2






 
fig1 = figure(1)
set(fig1,'Position',[10 200 300 300])
plot(wlcol,10*log10(outputPcol),'r-');grid on;
