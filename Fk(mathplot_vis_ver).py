import numpy as np
import math
import matplotlib.pyplot as plt


def ubahdegkerad (d):
    return d*math.pi/180.0

def R2():
    angle=ubahdegkerad(30)
    cos=math.cos(angle)
    sin=math.sin(angle)
    Rservo2 = np.array([[cos, -sin, 0],
                    [sin, cos, 0],
                    [0, 0, 1]])
    return Rservo2
    
def R1():
    angle=ubahdegkerad(40)
    cos=math.cos(angle)
    sin=math.sin(angle)
    Rservo1 = np.array([[cos, -sin, 0],
                        [sin,  cos, 0],
                        [0,  0, 1]])
    return Rservo1
    
def T1():
    #NIU=25/569826/TK/64173
    Tservo1 = np.array([[1, 0, 26],
                        [0, 1, 0],
                        [0, 0, 1]])
    return Tservo1
    
def T2():
    #NIU=25/569826/TK/64173
    Tservo2 = np.array([[1, 0, 73],
                        [0, 1, 0],
                        [0, 0, 1]])
    return Tservo2

Calculation1=np.dot(R2(), T2())
Calculation2=np.dot(T1(), Calculation1)
Final=np.dot(R1(), Calculation2)

x_servo2 = Final[0][2]
y_servo2 = Final[1][2]

posisi1 = np.dot(R1(), T1())
x_servo1 = posisi1[0][2]
y_servo1 = posisi1[1][2]


print(f"x servo 2 = {Final[0][2]}, y servo 2 = {Final[1][2]}")
print(f"x servo 1 = {x_servo1}, y servo 1 = {y_servo1}")

plt.figure()
plt.plot([0, x_servo1, x_servo2], [0, x_servo2, y_servo2], marker='o')
plt.title("Menampilkan hasil dengan matplotlib")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()

