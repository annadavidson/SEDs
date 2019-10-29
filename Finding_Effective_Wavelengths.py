# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:12:14 2019

@author: Anna
"""

#Defining a function to get the effective wavelength for 70 filters
import numpy as np
def finding_eff_waves():
    filterfile = ("FILTER.RES.GOGREEN") #file with filter fluxes
    f = open(filterfile, 'r')
    
    #make dictionary to hold all filter curves
    filtercurves ={}
    
    for line in f:
        #print(repr(line))                   #this prints all special characters
        #strip off special characters
        line = line.strip()
        #split on whitespaces
        cols = line.split()
        #print(cols)
    
        #find number of lines for next filter curve
        nlines = int(cols[0])               #converts string to integer
        filtname = cols[1]                   #name of that filter
        #initialize array for lambda and transmission
        lam = np.array([])
        trans = np.array([])
        #loop over every line in a given filter
        for iline in range(nlines):
            #reads in a single line
            transline = f.readline()
            #strip off special characters
            transline = transline.strip()
    
            #split line into a list of strings
            transcols = transline.split()
    
            #append each wavelength and transmission value to the lam and trans arrays
            lam = np.append(lam, float(transcols[1]))
            trans = np.append(trans, float(transcols[2]))
    
        #fill dictionary for each filter with the transmission curve for that filter, stored in its own dictionary
        filtercurves[filtname] = {'lam' : lam , 'trans' : trans}
    
    #print(filtercurves['g'], '\n')
    #print('wavelength of filter curve = ', filtercurves['g']['lam'])
    
    
    #Calulate effective wavelength:
    eff_wave = []  #initialize an array to store effective wavelengths
    i = 0
    for filt, data in filtercurves.items(): #for filt, parses through each filter, for data is there because it doesn't work otherwise
        #print('Filter: %s' % filt)
        wave = filtercurves[filt]['lam']
        tran = filtercurves[filt]['trans']
        mult = wave*tran
        num = np.trapz(mult, x=wave)
        denom = np.trapz(tran, x=wave)
        eff_wave.append(num/denom)  #append effective wavelengths to the array
        #print ("Effective", filt, "Wavelength: ", eff_wave[i],'\n')
        i = i+1
    return(eff_wave);
