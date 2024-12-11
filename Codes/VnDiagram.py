#V-n diagram:

#Importing libraries:
import sympy as sym
from scipy.optimize import fsolve
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

#Selecting the font size and type to be used in the figure.
font={ 'family' : 'Times New Roman',
       'weight' : 'normal',
       'size' : '16'}

#Setting the selected font properties.          
matplotlib.rc('font', **font)


p = 1.207
S = 0.9168
Clmax = 1.1460
Clmin = -1.1441
W = 8.2153*9.81
Vmax = 20.35

Vp = np.sqrt(2*3*W/(p*S*Clmax))
Vn = np.sqrt(2*1.5*W/(p*S*abs(Clmin)))

V_list1 = np.linspace(0, Vp, 100)
V_list2 = np.linspace(Vp,Vmax, 100)
V_list3 = np.linspace(0, Vn, 100)
V_list4 = np.linspace(Vn,Vmax, 100)
n_list_pos1 = np.zeros(len(V_list1))
n_list_neg1 = np.zeros(len(V_list3))
n_list_pos2 = np.zeros(len(V_list2))
n_list_neg2 = np.zeros(len(V_list4))


for i, V in enumerate(V_list1):
    n_list_pos1[i] = (0.5*p*Clmax*S*V*V/W)

for i, V in enumerate(V_list2):
    n_list_pos2[i] = 3

for i, V in enumerate(V_list3):
    n_list_neg1[i] = (0.5*p*Clmin*S*V*V/W)

for i, V in enumerate(V_list4):
    n_list_neg2[i] = -1.5


#Plotting Block:
plt.plot(V_list1, n_list_pos1, label = "Stall line")
plt.plot(V_list2, n_list_pos2, label = "Positive limit load factor")
plt.plot(V_list3, n_list_neg1, label = "Stall line")
plt.plot(V_list4, n_list_neg2, label = "Negative limit load factor")
plt.plot([V_list2[-1], V_list4[-1]], [n_list_pos2[-1], n_list_neg2[-1]], label = "Maximum dynamic pressure")


#Gust load diagram:
Clalpha_wing = 4.6352
Wg = 0.55*0.3048*15

term = 0.5*p*Clalpha_wing*Wg
term0 = W/S
V = np.linspace(0, Vmax, 50)

n_pos = 1+term*V/term0
n_neg = 1 - term*V/term0

plt.plot(V, n_pos, '.-', label = "Gust line: $W_g$ > 0, $U_{de} = 15$ ft/s")
plt.plot(V, n_neg, '.-', label = "Gust line: $W_g$ < 0, $U_{de} = 15$ ft/s")

###

Wg = 0.55*0.3048*20

term = 0.5*p*Clalpha_wing*Wg
V = np.linspace(0, 18, 50)

n_pos1 = 1+term*V/term0
n_neg1 = 1 - term*V/term0

plt.plot(V, n_pos1, '.-', label = "Gust line: $W_g$ > 0, $U_{de} = 20$ ft/s")
plt.plot(V, n_neg1, '.-', label = "Gust line: $W_g$ < 0, $U_{de} = 20$ ft/s")
plt.plot(np.linspace(V[-1], Vmax, 8), np.linspace(n_pos1[-1], n_pos[-1], 8), '.-')
plt.plot(np.linspace(V[-1], Vmax, 8), np.linspace(n_neg1[-1], n_neg[-1], 8), '.-')

###

plt.title("V-n Diagram")
plt.ylabel("n -->")
plt.xlabel(" V (m/s) -->")
plt.grid(linestyle = "--")
plt.legend(fontsize = '12', loc = (1.05,0))
plt.savefig("VnDiagram", dpi = 300, bbox_inches = 'tight')
plt.show()








