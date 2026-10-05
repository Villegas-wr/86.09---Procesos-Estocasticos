import numpy as np
import matplotlib.pyplot as plt

num_realizaciones = 1000
p = 0.5
N = 100

#####################################################

#      GENERACIÓN DE REALIZACIONES

#####################################################

# Partiendo siempre de una uniforme, aplico transformación para obtener la distribución deseada. Genero un matriz 1000 x 100 (realizaciones x muestras)

U = np.random.uniform(0, 1, (num_realizaciones, N)) 
Z = np.where(U < p, 1, 0)
X = 2 * Z - 1

mu_estimada = np.zeros(N)
var_estimada = np.zeros(N)

for n in range(0, N, 1):
    aux_mu = 0
    for r in range(0, num_realizaciones, 1):
        aux_mu += X[r,n] 

    mu_estimada[n] = aux_mu/num_realizaciones

    aux_var = 0
    for i in range(0, num_realizaciones, 1):
        aux_var += (X[i, n] - mu_estimada[n]) ** 2

    var_estimada[n] = aux_var/num_realizaciones



#####################################################

#      COMPARACIÓN ENTRE TEÓRICAS Y ESTIMADAS

#####################################################

mu_teo = 2 * p - 1
var_teo = 4 * p * (1- p)


#####################################################

#               GRÁFICOS COMPARATIVOS

#####################################################
n = np.arange(N)
r = 0

plt.figure()
plt.plot(n, X[r, :], label="Realización")
plt.plot(n, mu_teo * np.ones(N), label="Media teórica")
plt.xlabel("n")
plt.ylabel("X(n)")
plt.title(f"Realización {r} del proceso")
plt.legend()
plt.grid()
plt.show()



plt.figure()
plt.plot(n, mu_estimada, label="Media estimada")
plt.plot(n, mu_teo * np.ones(N), label="Media teórica")
plt.ylim(-1, 1)
plt.xlabel("n")
plt.ylabel("Media")
plt.title("Media estimada vs teórica")
plt.legend()
plt.grid()
plt.show()




plt.figure()
plt.plot(n, var_estimada, label="Varianza estimada")
plt.plot(n, var_teo * np.ones(N), label="Varianza teórica")
plt.ylim(-1, 1.2)
plt.xlabel("n")
plt.ylabel("Varianza")
plt.title("Varianza estimada vs teórica")
plt.legend()
plt.grid()
plt.show()