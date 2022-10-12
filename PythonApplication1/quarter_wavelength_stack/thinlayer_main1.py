

#Thinlayer_main1.py
#2022/10/7
# Takeshi Ozeki, Optical Curcit. p.89 multilayer dielectric film filters

import numpy as np
import matplotlib.pyplot as plt

import Thinlayer_def


startwl = 1.200 # [um]
stepwl = 0.002 # [um]

nn = 512 # number of sampling point

# Asssume quarter waelength
# 1550nm * 0.25 --> 387.5 nm
# 387.5nm/1.463 --> 264.866 nm
# 387.5nm/2.130 --> 181.924 nm

  
L1 = [0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866]

L2 = [0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924]

 
mm = len(L1)

print('Length of L1 = ')
print(mm)


no = 1.000 #refractive Index


wlcol = np.zeros(nn)
PTcol = np.zeros(nn)
PTdBcol = np.zeros(nn)
PRdBcol = np.zeros(nn)

for ii in range(nn):

    Ein = np.array([[1,0],[0,1]])
    
    wl = startwl + stepwl*ii
    wlcol[ii] = wl
    print(wl)

    n1 = 1.463 + 0.003827/(wl**2) + 0.000/(wl**4)
    n2 = 2.1305 + 0.018499/(wl**2) + 0.00199850/(wl**4)
    #ns = 1.6553 + 0.0086444/(wl**2) + 0.00081178/(wl**4)
    

    for jj in range(mm):

        print(jj)

        th1 = L1[jj]
        th2 = L2[jj]           

        E_intermedate = Thinlayer_def.dielectric(wl, n1, n2, th1, th2, Ein)
        Ein = E_intermedate
            
    PT1 = abs(E_intermedate[0,0])**2
    PR1 = abs(E_intermedate[1,0])**2
    
    PTcol[ii] = PT1
    PTdBcol[ii] = -10*np.log(PT1)
    PRdBcol[ii] = 10*np.log(PR1)



#print('Wavelength = ')
#print(wlcol)

#print('Power = ')
#print(TPcol)


fig = plt.figure(figsize = (10,4), facecolor='lightblue')

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.plot(wlcol,PTdBcol)
ax1.set_xlabel("Wavelength")
ax1.set_ylabel("Power")
#ax1.set_ylim(0,2)
ax1.grid()

ax2.plot(wlcol,PRdBcol)

plt.show()

#fig1 = figure(1)
#set(fig1,'Position',[10 200 300 300])
#plot(wlcol,10*log10(outputPcol),'r-');grid on;
