import numpy as np
import math

def ubahdegkerad (d):
    return d*math.pi/180.0

def R2(sudut2):
    angle=ubahdegkerad(sudut2)
    cos=math.cos(angle)
    sin=math.sin(angle)
    Rservo2 = np.array([[cos, -sin, 0],
                    [sin, cos, 0],
                    [0, 0, 1]])
    return Rservo2
    
def R1(sudut1):
    angle=ubahdegkerad(sudut1)
    cos=math.cos(angle)
    sin=math.sin(angle)
    Rservo1 = np.array([[cos, -sin, 0],
                        [sin,  cos, 0],
                        [0,  0, 1]])
    return Rservo1
    
def T1(ps1):
    #NIU=25/569826/TK/64173
    Tservo1 = np.array([[1, 0, ps1],
                        [0, 1, 0],
                        [0, 0, 1]])
    return Tservo1
    
def T2(ps2):
    #NIU=25/569826/TK/64173
    Tservo2 = np.array([[1, 0, ps2],
                        [0, 1, 0],
                        [0, 0, 1]])
    return Tservo2

panjang_T1=float(input("Masukkan panjang untk servo 1: "))
angle_R1=float(input("Masukkan sudut R1 (derajat): "))
panjang_t2 = float(input("Masukkan panjang untuk servo 2: "))
angle_R2=float(input("Masukkan sudut r2 (derajat): "))

Calculation1=np.dot(R2(angle_R2), T2(panjang_t2))
Calculation2=np.dot(T1(panjang_T1), Calculation1)
Final=np.dot(R1(angle_R1), Calculation2)





print(f"x= {Final[0][2]} dan y= {Final[1][2]}")




