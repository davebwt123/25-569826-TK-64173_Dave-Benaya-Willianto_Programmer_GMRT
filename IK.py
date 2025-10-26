import numpy as np
import math

def O2(x, y, L1, L2):
    isi2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    isi2 = np.clip(isi2, -1, 1)
    return np.arccos(isi2)  # radian

def O1(x, y, L1, L2, theta2):
    num = y*(L1 + L2*np.cos(theta2)) - x*(L2*np.sin(theta2))
    den = x*(L1 + L2*np.cos(theta2)) + y*(L2*np.sin(theta2))
    return np.arctan2(num, den)

L1 = float(input("Masukkan panjang lengan 1: "))
L2 = float(input("Masukkan panjang lengan 2: "))
x  = float(input("Masukkan x tujuan: "))
y  = float(input("Masukkan y tujuan: "))

# elbow-down solution
theta2 = O2(x, y, L1, L2)
theta1 = O1(x, y, L1, L2, theta2)

print(f"Derajat 1= {np.degrees(theta1)} , Derajat 2= {np.degrees(theta2)}")
