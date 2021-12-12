import numpy as np  # Mathematics module used mainly for arrays
import matplotlib.pyplot as plt  # Graphing module


class ObjConditions:  # Object created to store information
    SimulationStart = 0  # Start time of simulation
    Simulationlength = 7.884e+09  # End time of simulation in seconds, 250 years

    def __init__(self, Mass, X, Y, Vx, Vy):
        self.Mass = Mass
        self.X = X
        self.Y = Y
        self.Vx = Vx
        self.Vy = Vy

def CalOrbit2(Obj1, Obj2):
    t = ObjConditions.SimulationStart  # Time counter set to initial time
    tf = ObjConditions.Simulationlength  # Stores end time of simulation
    G = 6.67408 * (10 ** -11)  # Gravitational constant
    h = 86400  # Step size for euler method, is the time change of the simulation delta t

    # Arrays to store the x and y positions of the two plants
    x_plt = np.array([])
    y_plt = np.array([])
    x_pltSun = np.array([])
    y_pltSun = np.array([])

    while t < tf:
        Obj1.X = Obj1.X + Obj1.Vx * h  # Uses variables from last iteration to calculate cordinates of next
        Obj1.Y = Obj1.Y + Obj1.Vy * h  # Euler method for calculating for cordinates

        Obj2.X = Obj2.X + Obj2.Vx * h  # Euler method but for cordinates for object2
        Obj2.Y = Obj2.Y + Obj2.Vy * h

        rx = Obj1.X - Obj2.X  # Distances between the planets
        ry = Obj1.Y - Obj2.Y

        r = np.sqrt(rx ** 2 + ry ** 2)  # Unit vector of distance

        Obj1.Vx = Obj1.Vx - h * (G * Obj2.Mass * rx) / r ** 3  # Velocities gained by object1 from object2
        Obj1.Vy = Obj1.Vy - h * (G * Obj2.Mass * ry) / r ** 3

        momJX = Obj1.Vx * Obj1.Mass  # Calculates the momentum in x and y for second planet
        momJY = Obj1.Vy * Obj1.Mass

        Obj2.Vx = momJX / Obj2.Mass  # Velocities gained by object2 from object1
        Obj2.Vy = momJY / Obj2.Mass

        x_plt = np.append(x_plt, Obj1.X)  # Append new distance to the arrays for both objects
        y_plt = np.append(y_plt, Obj1.Y)
        x_pltSun = np.append(x_pltSun, Obj2.X)
        y_pltSun = np.append(y_pltSun, Obj2.Y)

        t = t + h  # increases the time by the step size so that the simulation advances

    return x_plt, y_plt, x_pltSun, y_pltSun


# Changes how the plots look including text
font = {'family': 'serif',
        'color': 'darkred',
        'weight': 'normal',
        'size': 16,
        }

plt.style.use('classic')
# Creates two object for the initial conditions for each gravitional body then calls function passing the objects
Sun = ObjConditions(1.989*(10**30),0,0,0,0)
Jupiter = ObjConditions(1.89819*(10**27),-7.4052442*(10**11),0,0,-13720)
x_pltJ, y_pltJ, x_pltSunJ, y_pltSunJ = CalOrbit2(Jupiter,Sun)

# Passes Saturn instead of Jupiter to the function
Sun = ObjConditions(1.989*(10**30),0,0,0,0)
Saturn = ObjConditions(5.6834*(10**26),-1.3525635*(10**12),0,0,-10180)
x_pltS, y_pltS, x_pltSunS, y_pltSunS = CalOrbit2(Saturn,Sun)
# Plots the orbit's of Saturn and Jupiter around the Sun at 0,0
plt.plot(x_pltS, y_pltS, "-b", label="Saturn")
plt.plot(x_pltJ, y_pltJ, "-g", label="Jupiter")
plt.plot(0, 0, 'ro')
plt.legend(loc="upper right")
plt.title('Saturn\'s and Jupiter\'s orbit around the Sun', fontdict=font,fontsize=12)
plt.xlabel('X distance (m)', fontdict=font) # Axis' lables
plt.ylabel('Y distance (m)', fontdict=font)
plt.show()
print(x_pltS)