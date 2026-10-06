import numpy as np
import matplotlib.pyplot as plt

num_realizaciones = 10

w = 0.015
mu_A = 1
var_A = 0.16

periodo_muestras = (2 * np.pi)/w
N = int(np.ceil(2 * periodo_muestras))

#################################################

#           Generación de proceso

#################################################

# Partiendo siempre de una uniforme obtengo la distribución normal usando transformación Box-Muller. 
# Como la amplitud A se mantiene constante en el tiempo, únicamente se renueva en el cambio de número de realización.

X = np.zeros((num_realizaciones, N))

max_A = 0

for r in range(0, num_realizaciones, 1):

    U_1 = np.random.uniform(0, 1)
    U_2 = np.random.uniform(0, 1)

    Z = np.sqrt(-2 * np.log(U_1)) * np.cos(2 * np.pi * U_2)
    A = mu_A + np.sqrt(var_A) * Z

    if(np.abs(A) > max_A):
        max_A = A

    for k in range(0, N, 1):
        X[r, k] = A * np.sin(w * k)


#################################################

#           Gráfico comparativo

#################################################

n = np.arange(N)
mu_X_teo = mu_A * np.sin(w * n)


plt.figure()

for r in range(0, num_realizaciones, 1):
    plt.plot(n, X[r, :])

plt.plot(n, mu_X_teo, color= "black", linewidth= 2, label="Media teórica")
plt.xlabel("n")
plt.ylabel("X(n)")
plt.title("Proceso X(n) = A sen(won)")
plt.xlim(0, N - 1)
plt.ylim(-1.1 * max_A, 1.1 * max_A)
plt.legend()
plt.grid()
plt.show()

