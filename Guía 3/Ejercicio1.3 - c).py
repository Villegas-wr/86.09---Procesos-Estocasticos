import numpy as np
import matplotlib.pyplot as plt

num_realizaciones = 1000
N = 200
n = np.arange(N)

X = np.zeros((num_realizaciones, N))

# Como se desea que A y B sean constantes en el tiempo tengo que recorrer el loop de forma que unicamente se renueven los valores aleatorios en la proxima realización

for r in range(0, num_realizaciones, 1):

    A = np.random.uniform(0, 1)
    B = np.random.uniform(0, 1)

    for k in range(0, N, 1):
        X[r, k] = A * k + B

mu_teo = n / 2 + 0.5
var_teo = (n ** 2) / 12 + 1 / 12

mu_estimada = np.zeros(N)
var_estimada = np.zeros(N)

for k in range(0, N, 1):

    aux_mu = 0
    aux_var = 0

    for r in range(0, num_realizaciones, 1):
        aux_mu += X[r, k] 

    mu_estimada[k] = aux_mu / num_realizaciones

    for r in range(0, num_realizaciones, 1):
        aux_var += (X[r, k] - mu_estimada[k]) ** 2

    var_estimada[k] = aux_var / num_realizaciones


plt.figure()

plt.plot(n, mu_estimada, label= "Media estimada")
plt.plot(n, mu_teo, label= "Media teorica")
plt.xlabel("n")
plt.ylabel("Media")
plt.title("Proceso X(n) = An + B")
plt.legend()
plt.grid()
plt.show()

plt.figure()

plt.plot(n, var_estimada, label= "Varianza estimada")
plt.plot(n, var_teo, label= "Varianza teorica")
plt.xlabel("n")
plt.ylabel("Varianza")
plt.title("Proceso X(n) = An + B")
plt.legend()
plt.grid()
plt.show()