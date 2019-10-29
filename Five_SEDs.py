# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:48:11 2019

@author: Anna
"""

from matplotlib import pyplot as plt
from astropy.io import ascii
import numpy as np

path = r'''C:\Users\Anna\Learning-Python-master'''
zfile = path + r'''\compilation_SpARCS-0035.dat'''
zdat = ascii.read(zfile)
photfile = path + r'''\SpARCS-0035_totalall_HAWKIKs.cat'''
photdat = ascii.read(photfile)


#this prints out all the spec-z values and also pulls values for the same objects from the observed photometry files.
#for i in range(len(photdat['id'])):
#    print(photdat['id'][i],zdat['PHOTCATID'][i],zdat['spec_z'][i])
    #you *could* put an if statement here to test if an object has a spec-z
#print(data)
#print(data['PHOTCATID'][1],data['spec_z'][1])
#a better way is to use the numpy.where() command
#this is an array of all indices which satisfy the condition in the ()

good_flux = 10**0.8
izspec = np.where((zdat['spec_z'] > 0) & (photdat['totmask'] == 0) & (photdat['K_flag'] == 0) & (photdat['HAWKIKs'] > good_flux))
izspec = izspec[0]
#print("Chosen Galaxy ID's:",izspec)
#print(zdat['spec_z'][1202])

#this prints the rows of the two tables that correspond to these indices
#print(photdat['id'][izspec],zdat['PHOTCATID'][izspec],zdat['spec_z'][izspec])

#Calling the function finding_eff_waves into an array of effective wavelengths
from Finding_Effective_Wavelengths import finding_eff_waves
eff_waves = finding_eff_waves()
#print(eff_waves)

#Getting flux in each filter for 5 galaxies
#filt_names = HAWKIKs,VIMOSU,VIMOSB,VIMOSV,VIMOSR,VIMOSI,DECamz,FOURSTARJ1,HAWKIJ,IRAC1,IRAC2,IRAC3,IRAC4 
g = [1201,2225,3114,4443,4810] #indices for 5 random galaxies
fnu = [[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13]]
for i in range(len(g)):
    fnu[i] = photdat['HAWKIKs'][g[i]],photdat['VIMOSU'][g[i]],photdat['VIMOSB'][g[i]],photdat['VIMOSV'][g[i]],photdat['VIMOSR'][g[i]], photdat['VIMOSI'][g[i]], photdat['DECamz'][g[i]],photdat['FOURSTARJ1'][g[i]],photdat['HAWKIJ'][g[i]],photdat['IRAC1'][g[i]],photdat['IRAC2'][g[i]],photdat['IRAC3'][g[i]],photdat['IRAC4'][g[i]]
        #print(photdat['HAWKIKs'][g[i]])
#print(fnu)

index = [39,26,27,28,29,30,45,32,37,40,41,42,43]
g_wave = [1,2,3,4,5,6,7,8,9,10,11,12,13] #dummy values
for i in range(len(index)):
    g_wave[i] = eff_waves[index[i]]   
g_wave = np.array(g_wave)
#print(g_wave)

#print(fnu[0])
fnu = np.array(fnu)
print(fnu[0])
f = fnu
f=np.array(f)
#Finding fnu from the catalog flux, which is a ratio of fnu over f(m=25)
for i in fnu:
    for j in i:
        f = fnu*(10**(-29.432))
print(f[0])

#Converting to flambda
flambda = f #placeholder values
flambda = np.array(flambda)
for i in f:
    for j in i:
        flambda = (f*299000000.0)/((g_wave*(10**-10))**2)
print(flambda[0])

    
#fnu_non_rat = fnu*(10**(-29.432))
#fnu_non_rat = np.array(fnu_non_rat)
#print(fnu_non_rat[0])
#flambda = np.array((fnu_non_rat*299000000.0)/(g_wave**2))
#print(flambda)

#for i in range(5):
#    plt.scatter(g_wave, flambda[0])
 
g_freq = (2.99*10**8)/(g_wave*(10**-10))   
print (g_freq)

#for i in range(5):
#    plt.scatter(g_freq,fnu[i])
    



z = np.sqrt(g_freq**2 + fnu[0]**2)

plt.subplot(321)
plt.scatter(g_freq, fnu[0], s=80, c=z, marker=(5,1))

plt.subplot(322)
plt.scatter(g_freq, fnu[1], s=80, c=z, marker=(5, 1))

plt.subplot(323)
plt.scatter(g_freq, fnu[2], s=80, c=z, marker=(5, 1))

plt.subplot(324)
plt.scatter(g_freq, fnu[3], s=80, c=z, marker=(5,1))

plt.subplot(325)
plt.scatter(g_freq, fnu[4], s=80, c=z, marker=(5, 1))

plt.show()

    
    
    
    