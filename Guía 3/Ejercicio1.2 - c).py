import numpy as np
import matplotlib.pyplot as plt

num_realizaciones = 1000
N = 50
p = [0.2, 0.5, 0.8]
n =  np.arange(N + 1)

# Partiendo siempre de una uniforme, aplico transformación para obtener la distribución deseada. Como tengo que probar con distintos valores de probabilidad
# debo de trabajar en un for que abarque las opciones luego generar las expresiones en función de la probabilidad actual en el loop. 


for i in range(0, len(p), 1):
    U = np.random.uniform(0, 1, (num_realizaciones, N)) 
    Z = np.where(U < p[i], 1, 0)
    X = 2 * Z - 1
    Y = np.zeros((num_realizaciones, N+1))

    for r in range(0, num_realizaciones, 1):
        for k in range(0, N, 1):
            Y[r, k + 1] = Y[r, k] +  X[r, k]


    # Vectores de media teoricos usando la probabilidad actual en el loop. 
    mu_teo = n * (2 * p[i] - 1)
    var_teo = 4 * n * p[i] * (1 - p[i])


    # Estimación de media y varianza
    mu_estimada = np.zeros(N + 1)
    var_estimada = np.zeros(N + 1)

    for k in range(0, N + 1, 1):
        aux_mu = 0
        aux_var = 0

        for r in range(0, num_realizaciones, 1):
            aux_mu += Y[r, n]

        mu_estimada = aux_mu/num_realizaciones

        for r in range(0, num_realizaciones, 1):
            aux_var += (Y[r, n] - mu_estimada) ** 2

        var_estimada = aux_var/num_realizaciones


    # Gráficos de cada realización r
    plt.figure()

    plt.plot(n, mu_estimada, label="Media estimada")
    plt.plot(n, mu_teo, label="Media teórica")
    plt.xlabel("n")
    plt.ylabel("Media")
    plt.title(f"Random walk - p = {p[i]}")
    plt.legend()
    plt.grid()
    plt.show()



    plt.figure()

    plt.plot(n, var_estimada, label="Varianza estimada")
    plt.plot(n, var_teo, label="Varianza teórica")
    plt.xlabel("n")
    plt.ylabel("Varianza")
    plt.title(f"Random walk (varianza) - p = {p[i]}")
    plt.legend()
    plt.grid()
    plt.show()


