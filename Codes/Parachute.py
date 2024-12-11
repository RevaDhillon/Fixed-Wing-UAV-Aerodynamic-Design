#Parachute landing calculations:

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

#RK4 Method:
def RK4(fun, dt, X0):

    f1 = fun(X0)
    f2 = fun(X0 + 0.5*dt*f1)
    f3 = fun(X0 + 0.5*dt*f2)
    f4 = fun(X0+dt*f3)

    X_out = X0 + dt*(f1 + 2*f2 + 2*f3 + f4)/6

    return X_out

#Equations to solve:
def Equations(X):
  dx = X[2]
  dz = X[3]
  ddx = -a*X[2]*np.sqrt(X[2]*X[2] + X[3]*X[3])
  ddz = g - a*X[3]*np.sqrt(X[2]*X[2] + X[3]*X[3])
  return np.array([dx, dz, ddx, ddz])

#Initializations:
X0 = np.array([0, -20, 13.68, 0]) #Initial conditions
g = 9.81
a = g/(3.14**2)
dt = 0.01
N = 670

X = np.zeros([4, N])#Storage matrix
t = np.zeros(N)
X[:, 0] = X0

for i in range(N-1):

  t[i+1] = (i+1)*dt

  Xout = RK4(Equations, dt, X0)
  X[:, i+1] = Xout
  X0 = Xout
 
#Plotting Block:
plt.plot(t, X[0])
plt.title("The x location with time:")
plt.ylabel("x (m) -->")
plt.xlabel("Time t (s) -->")
plt.grid(linestyle = "--")
plt.savefig("Xt", dpi = 300, bbox_inches = 'tight')
plt.show()

plt.plot(t, abs(X[1]))
plt.title("The z location with time:")
plt.ylabel("|z| (m) -->")
plt.xlabel("Time t (s) -->")
plt.grid(linestyle = "--")
plt.savefig("Zt", dpi = 300, bbox_inches = 'tight')
plt.show()

plt.plot(t, X[2])
plt.title("The x velocity with time:")
plt.ylabel("$\\dot{x}$ (m/s) -->")
plt.xlabel("Time t (s) -->")
plt.grid(linestyle = "--")
plt.savefig("Xvelt", dpi = 300, bbox_inches = 'tight')
plt.show()

plt.plot(t, X[3])
plt.title("The z velocity with time:")
plt.ylabel("$\\dot{z}$ (m/s) -->")
plt.xlabel("Time t (s) -->")
plt.grid(linestyle = "--")
plt.savefig("Zvelt", dpi = 300, bbox_inches = 'tight')
plt.show()

plt.plot(X[0], abs(X[1]))
plt.title("The Trajectory:")
plt.ylabel("|z| (m) -->")
plt.xlabel("x (m) -->")
plt.grid(linestyle = "--")
plt.savefig("Traj", dpi = 300, bbox_inches = 'tight')
plt.show()






