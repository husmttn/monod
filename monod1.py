"""
Approximation de la concentration bacterienne au bout de 10h dans un milieu glucosee
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import *
def monod(h,phi,xtn,r,k): 
 return (xtn+(((h*phi*(((xtn-x0)/-
r)+s0))/((k+(xtn-x0)/-r)+s0))*xtn))
l=[] 
x0=0.1
s0=1
xtn=0.1
phi=0.0437
h=1
r=0.68
k=0.085
fxtn=0
for i in range (1,100): 
 fxtn = monod(h, phi, xtn, r, k)
 l.append(fxtn)
 xtn = fxtn
 
fig=plt.figure() 
fig.patch.set_facecolor('xkcd:grey') 
plt.plot(l,'r')
plt.plot(10,l[10],"-bo")
print("A t=10 nous avons ",l[10],"mg/L")
plt.axis([0,100,0.1,0.8])
plt.xlabel("Temps(en h)")
plt.ylabel("Concentration de bactérie en mg/l")
plt.title("Concentration de bactérie")