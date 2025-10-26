import math


L1 = float(input("Masukkan panjang untk servo 1: "))
L2 = float(input("Masukkan panjang untk servo 2: "))
derajat1 = float(input("Masukkan sudut R1 (derajat): "))
derajat2 = float(input("Masukkan sudut R2 (derajat): "))


t1 = math.radians(derajat1)
t2 = math.radians(derajat2)


x = L1 * math.cos(t1) + L2 * math.cos(t1 + t2)
y = L1 * math.sin(t1) + L2 * math.sin(t1 + t2)

print(f"x = {x} dan y = {y}")