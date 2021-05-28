"""
On suppose que l’expérience se déroule dans un réservoir de 100 m3 brassé en 
permanence
Et qu’en permanence de l’eau glucosée arrive en remplacement de l’eau polluée du 
milieu à raison de 1 l.s-1

On suppose qu’à chaque seconde, 1l d’eau glucosée avec une concentration de 1 mg.l-1 se rajoute et 1l d’eau polluée sort

Étudions la biomasse en sortie de réservoir lorsqu’elle tend vers un équilibre

Pour en savoir plus lire le rapport pdf.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from pylab import *
def bacterie(stn,s0,x0,r): 
    return (-r)*(stn-s0)+x0
def glucose(xtn,s0,x0,r): 
    return ((xtn-x0)/(-r))+s0
def monod(h,phi,xtn,r,k): 
    return (xtn+(((h*phi*(((xtn-x0)/-r)+s0))/((k+(xtn-x0)/-r)+s0))*xtn))
l1=[] 
l2=[]
x0=0.1
s0=1
xtn=0.1
stn=1
r=0.68
phi=0.0437
h=1
k=0.085
c=100
x=arange(1,10000,100)
for i in x: 
    stn = glucose(xtn, s0, x0, r)
    xtn = bacterie(stn, s0, x0, r)
    l1.append(xtn-(xtn/100000)*3600)
    l2.append(stn-((stn/100000)*3600)+0.036)
    a=stn-xtn 
    if abs(a)<c:
        b=i/100
        c=a
    xtn=monod(h, phi, xtn, r, k)
 
fig=plt.figure() 
fig.patch.set_facecolor('xkcd:grey') 
print ("le point d'équilibre se trouve pour t=",b)
plt.plot(l1,"b")
plt.plot(l2,"r")
plt.axis([0,100,0,1.1])
plt.xlabel("Temps(en h)")
plt.ylabel("Concentration en mg/l")
plt.title("Le point d'équilibre")
