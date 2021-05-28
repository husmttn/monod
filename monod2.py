"""
Recherche du temps lorseque la concentration bacterienne ateint 1 g.l-1
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import *
def monod(h,phi,xtn,r,k): 
    return (xtn+(((h*phi*s0))/((k+s0))*xtn))
def date(n): 
    j=n//24
    h=n%24
    print("soit",j,"jours et",h,"heures.")
l=[] 
x0=0.1
s0=1
xtn=0.1
phi=0.0437
h=1
r=0.68
k=0.085
fxtn=0
a=0
b=100000
c=0
for i in range (1,300): 
    fxtn = monod(h, phi, xtn, r, k)
    l.append(fxtn)
    xtn = fxtn
    a=abs(l[i-1]-1000)
    if a<b:
        b=a
        c=i-1
print("On obtient une concentration de 1 g/L au bout de",c,"heures,") 
d=date(c)
fig=plt.figure()
fig.patch.set_facecolor('xkcd:grey') 
plt.plot(l,"r") 
plt.axis([0,300,0,5000]) 
plt.plot(c,l[c],"-bo")
plt.xlabel("Temps(en h)")
plt.ylabel("Concentration de Bactérie en mg/l")
plt.title("Biomasse de bactérie avec substrat constant")