#Weight Estimation:


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
       'size' : '14'}

#Setting the selected font properties.          
matplotlib.rc('font', **font)


#Data for the aircraft:
AR = 5.84112
S = 1.07
LDmax = 16.54
CLmax = 1.5

#kg
W0 = 12.142
Wb1 =  0.048 
W0_old = 1000
Wp = 1.5

n_prop = 0.478

e = 1.78*(1-0.045*(AR**0.68)) - 0.64
K = 1/(np.pi*e*AR)
CD0 = 0.25/(K*LDmax*LDmax)
gamma = 5*np.pi/180

En_dens = 269.79 #Wh/kg

A = 0.894172
L = -0.086047


#Storage variables:
W0_iter = []
n_iter = []
i = 0


#To obtain the battery specifications:
def ret_Wb(W0):

    W0 = W0*9.81 #Newton
    
    #Climb-1:
    v_cl1 = 1.2*np.sqrt(2*W0/(1.225*S*CLmax))
    L = W0*np.cos(gamma)
    CL = 2*L/(1.225*S*v_cl1*v_cl1)
    D = 0.5*1.225*S*v_cl1*v_cl1*(CD0 + K*CL*CL)
    T = W0*np.sin(gamma) + D
    Pcl1 = T*v_cl1
    Ecl1 = Pcl1*120/3600

    #Cruise:
    v_cruise = 18
    CL = 2*W0/(1.207*v_cruise*v_cruise*S)
    T = 0.5*1.207*v_cruise*v_cruise*S*(CD0 + K*CL*CL)
    Pcr = T*v_cruise
    Ecr = Pcr*2700/3600

    #Loiter:
    v_loit = v_cl1
    CL = 2*W0/(1.225*v_loit*v_loit*S)
    D = 0.5*1.225*v_loit*v_loit*S*(CD0 + K*CL*CL)
    Ploit = D*v_loit
    Eloit = Ploit*(540/3600)

    #Climb-2:
    W0 = W0 - 1.5*9.81
    v_cl2 = 1.2*np.sqrt(2*(W0)/(1.225*S*CLmax))
    L = W0*np.cos(gamma)
    CL = 2*L/(1.225*S*v_cl2*v_cl2)
    D = 0.5*1.225*S*v_cl2*v_cl2*(CD0 + K*CL*CL)
    T = W0*np.sin(gamma) + D
    Pcl2 = T*v_cl2
    Ecl2 = Pcl2*120/3600

    #Descent:
    Edes = Ecl1

    #Total:
    Etot1 = Ecl1 + Ecr + Eloit + Ecl2 + Edes

    #Miscellaneous requirements:
    Emis = 0.2*Etot1

    #Final energy:
    Ereq = 1.2*Etot1
    Efinal = Ereq/n_prop

    #Battery weight and number:
    W_battery = Efinal/En_dens
    Battery_number = math.ceil(W_battery/Wb1)
    W_battery = Battery_number*Wb1

    return W_battery, Battery_number


#Iterations for W0:
for j in range(3000):
    if(i%10 == 0):
        n_iter.append(i)
        W0_iter.append(W0)

    i = i + 1
        
    W0_old = W0
    Wb, nb = ret_Wb(W0) 
    W0 = Wp/(1 - (Wb/W0) - A*(W0**L))


#Output Block:   
print("Final DTOW: " + str(W0) + " kg")
print("Final number of batteries: " + str(nb))
print("Final battery weight: " + str(Wb) + " kg")


#Plotting Block:
plt.plot(n_iter, W0_iter, '.-')
plt.title("Iterations for DTOW $W_0$")
plt.ylabel("DTOW  $W_0$ (kg)-->")
plt.xlabel("Iteration number -->")
plt.grid(linestyle = "--")
plt.savefig("W0iter", dpi = 300, bbox_inches = 'tight')
plt.show()




