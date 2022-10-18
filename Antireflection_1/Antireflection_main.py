#Antireflection_main.py

import math
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

nn = 512 # number of sampling point

 
 
 %__________________________________________________              
 n0 = 1.000;


 layer1 = np.array([0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866, 0.264866])

 L2 = np.array([0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924, 0.181924])

 
 len_layer1 = len(layer1)
 print('Length of L1 = ')
 print(len_layer1)
 
  
  global wlcol 
  global dBTcol 
  global dBRcol 

  wlcol= np.zeros(mm,1);
  dBTcol=np.zeros(mm,1);
  dBRcol=np.zeros(mm,1);

 Mjj = [];
 
 for ii = 1:mm:

    wl = startwl + stepwl *ii

    wlcol(ii,1) = wl
    
     nL = 1.463 + 0.003827/(wl.^2) + 0.000./(wl.^4);
     nH = 2.1305 + 0.018499/(wl.^2) + 0.00199850./(wl.^4);
	nQuartz = 1.6553 + 0.0086444/(wl.^2) + 0.00081178./(wl.^4);
	#nLN = sqrt(2.23413 + ((2.68312-wl.^2)/(wl.^2-0.04481)) + ((2.59121.* wl)/(wl - 109.776)));
 
  #substrate: quartz
  ns = nQuartz;
 
  
 for kk = 1:ll:
       
         TM_intermedate = Antireflection_def.transfermatrix(wl, n1, n2, th1, th2, TMin)

       #print(jj)

        th1 = L1[jj]
        th2 = L2[jj]           

        TM_intermedate = Thinlayer_def.dielectric(wl, n1, n2, th1, th2, TMin)
        TMin = TM_intermedate
        #print(E_intermedate)
    
   TMout = TM_intermedate
    
   Eout2 = np.dot(TMout, Ein)

   Eout2_x = Eout2[0,0]
   Eout2_y = Eout2[1,0]
   
   Pow1 = np.abs(Eout2_x)**2
   Pow2 = np.abs(Eout2_y)**2  

   P1dBcol[ii] = -10*np.log(Pow1)
   P2dBcol[ii] = 10*np.log(Pow2)















       	if layer(kk) == 0
	        n = nL; #% L 
     	   
	     elseif   layer(kk) == 1
	        n = nH; #% H 

	      elseif   layer(kk) == 'A'
	        n = n0; #% AH 
   		end

     h(kk) =  (centerwl ./ n) .* thkpara(kk);   # thickness is quarter !!!
     sigma = 2 * math.p i *n*h(kk) / wl;   
        
   	Mjj = [math.cos(sigma), 1j*math.sin(sigma) / n;
      1j*n * math.sin(sigma), math.cos(sigma)]; 
              
              if kk ==1
               Morig = eye(2,2);
              end;
              
       M = Morig * Mjj;       
       Morig = M;
       
	end
            
     m11 = Morig(1,1);
     m12 = Morig(1,2);
     m21 = Morig(2,1);
     m22 = Morig(2,2);     
     t = (2*n0) ./ ((m11 + m12*ns)*n0 + (m21 + m22*ns));
  	       
  T = t*conj(t) * (ns/n0);

  dBTcol(ii,1) = 10*log10(T);
  
  B = m11 + m12*ns;
  C = m21 + m22 * ns;
  r = (n0*B - C) ./ (n0 * B + C);
  R = r * conj(r);
  
  dBRcol(ii,1) = 10*log10(R)


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