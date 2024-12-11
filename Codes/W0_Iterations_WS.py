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

###
CLmax = 1.5
v_cruise = 18

#kg
W0 = 12.142
Wb1 =  0.048 
W0_old = 1000
Wp = 1.5

n_prop = 0.478

e = 1.78*(1-0.045*(AR**0.68)) - 0.64
K = 1/(np.pi*e*AR)
CD0 = 0.25/(K*LDmax*LDmax)

gamma = 7*np.pi/180

En_dens = 269.79 #Wh/kg
b = 2.5

A = 0.894172
L = -0.086047
###

#Storage variables:
W0_iter = []
n_iter = []
i = 0

#Function for wing loading:
def WingLoading(W0, CD0, K):

    W0 = W0*9.81
    CL = np.sqrt(CD0/K)
    W_S = 0.5*1.207*v_cruise*v_cruise*CL
    Sref = W0/W_S
    Swet = 3*Sref
    ARref = b*b/Sref
    ARwet = b*b/Swet
    LDmax = 5.339*np.sqrt(ARwet) + 9.0769

    e = 1.78*(1-0.045*(ARref**0.68)) - 0.64
    K = 1/(np.pi*e*ARref)
    CD0 = 0.25/(K*LDmax*LDmax)

    return W_S, Sref, K, CD0
    

#To obtain the battery specifications:
def ret_Wb(W0, S, K, CD0):

    W0 = W0*9.81 #Newton
    
    #Climb-1:
    v_cl1 = 2/np.sin(gamma) 
    L = W0*np.cos(gamma)
    CL = 2*L/(1.225*S*v_cl1*v_cl1)
    D = 0.5*1.225*S*v_cl1*v_cl1*(CD0 + K*CL*CL)
    Tcl1 = W0*np.sin(gamma) + D
    Pcl1 = Tcl1*v_cl1
    Ecl1 = Pcl1*100/3600

    #Cruise:
    v_cruise = 18
    CL = 2*W0/(1.207*v_cruise*v_cruise*S)
    T = 0.5*1.207*v_cruise*v_cruise*S*(CD0 + K*CL*CL)
    Pcr = T*v_cruise
    Ecr = Pcr*2777.77/3600

    #Fly-by:
    v_flyby = 0.76*v_cruise
    CL = 2*W0/(1.225*v_flyby*v_flyby*S)
    T = 0.5*1.207*v_flyby*v_flyby*S*(CD0 + K*CL*CL)
    Pfb = T*v_flyby
    Efb = Pfb*400/3600

    #Climb-2:
    W0 = W0 - 1.5*9.81
    v_cl2 = v_cl1 
    L = W0*np.cos(gamma)
    CL = 2*L/(1.225*S*v_cl2*v_cl2)
    D = 0.5*1.225*S*v_cl2*v_cl2*(CD0 + K*CL*CL)
    T = W0*np.sin(gamma) + D
    Pcl2 = T*v_cl2
    Ecl2 = Pcl2*100/3600

    #Descent:
    Edes = Ecl1

    #Total:
    Etot1 = Ecl1 + Ecr + Efb + Ecl2 + Edes

    #Miscellaneous requirements:
    Emis = 0.2*Etot1

    #Final energy:
    Ereq = 1.2*Etot1
    Efinal = Ereq/n_prop

    #Battery weight and number:
    W_battery = Efinal/En_dens
    Battery_number = math.ceil(W_battery/Wb1)
    W_battery = Battery_number*Wb1

    return W_battery, Battery_number, Ecl1, Ecr, Efb, Ecl2, Tcl1


#Iterations for W0:
for j in range(3000):
    if(i%10 == 0):
        n_iter.append(i)
        W0_iter.append(W0)

    i = i + 1

        
    W0_old = W0
    W_S, S, K, CD0 = WingLoading(W0, CD0, K)
    Wb, nb, Ecl1, Ecr, Efb, Ecl2, Tcl1 = ret_Wb(W0, S, K, CD0) 
    W0 = Wp/(1 - (Wb/W0) - A*(W0**L))


#Output Block:
print("\n \n \n")
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




