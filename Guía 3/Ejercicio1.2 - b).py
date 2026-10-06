import numpy as np
import matplotlib.pyplot as plt

num_realizaciones = 5
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

    # Gráficos de cada realización r

    plt.figure()
    for r in range(0, num_realizaciones, 1):
       plt.plot(n, Y[r, :], label=f"Realización {r}")

    plt.plot(n, mu_teo, label="Media teórica")
    plt.xlabel("n")
    plt.ylabel("Y(n)")
    plt.title(f"Random walk - p = {p[i]}")
    plt.legend()
    plt.grid()
    plt.show()


