from math import * #Importar el conjunto de operaciones matemáticas complejas 
import matplotlib.pyplot as plt
h = 0.01
T_limite = 1000
n = T_limite/h
a = 0.4
b = 0.5
c = 0.3
d1 =1.0
k = 1.0
x_0 = 1
y_0 = 1
z_0 = 1
i=0
x = int(n+1) * [0]
y = int(n+1) * [0]
z = int(n+1) * [0]
x[0] = x_0
y[0] = y_0
z[0] = z_0
f_0 = 0
while(i <= n-1):
    x[i+1] = x[i] + (h*(y[i]))
    y[i+1] = y[i] + (h*(z[i]))
    if x[i+1] > 1:
        f_0 = k
    elif abs(x[i+1]) <= 1:
        f_0 = x[i+1]
    else:
        f_0 = -1*k
    z[i+1] = z[i] + (h*((-a*x[i])+(-b*y[i])+(-c*z[i])+(d1*f_0)))
    i = i+1
plt.plot(x,y)
plt.show()