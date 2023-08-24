#Generar polinomios de Taylor para e^x - FORMA SIMBÓLICA
#Se considera f(x) alrededor de x_0 = 0

import numpy as np
import math as math
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols("x") #Cada 'x' se considera como un simbolo solamente

#Funcion para obtener el polinomio de forma simbólica

def pol_taylor(n):
    #"n" es el grado del polinomio que se desea (primer polinomio, segundo polinomio, etc... Mientras mayor sea el grado, mayor sera la aproximacion)
  pol_taylor = 1
  for i in range(1, n+1):
    pol_taylor += (x**i)/math.factorial(i) #También: pol_taylor = pol_taylor + (x**i)/math.factorial(i)
  return pol_taylor

n = int(input('Defina el grado del polinomio: ')) #El susuario ingresa el grado del polinomio
a = float(input('Defina el limite superior "a" del intervalo [a, b]: ')) #El usuario ingresa el limite superior del intervalo
b = float(input('Define el limite inferior "b" del intervalo [a, b]: ')) #El usuario ingresa el limite inferior del intervalo

polinomio_graficar = sp.lambdify(x, pol_taylor(n)) #"lambdify" permite mapear la funcion que esta en matemática simbólica"

print(f'\nEl polinomio de Taylor de grado {n} para e^x es:\n')

x0 = np.arange(a, b, 0.0001) #Arreglo (intervalo) de puntos para evaluar la funcion (desde 'a' hasta 'b' en pasos de 0.0001)

#Graficación de la funcion con 'matplotlib'

plt.plot(x0, polinomio_graficar(x0), color = "blue", label = f"$P_{n}(x)$")
plt.title(f"Polinomio de Taylor (grado {n}) para $e^x$", fontsize = 15)
plt.xlabel("$x$", fontsize = 15)
plt.ylabel("$f(x)$", fontsize = 15)
plt.legend(fontsize = 15)
plt.grid()

pol_taylor(n) #Imrpime el polinomio de forma simbólica