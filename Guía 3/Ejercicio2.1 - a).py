import numpy as np
import matplotlib.pyplot as plt

num_realizaciones = 10
T = 5                   # Con valores más altos no se llega a apreciar la exponencial
t_n = 0.1               # Tiempo de muestreo debe de ser un valor chico para que el gráfico se vea suave y no estructurado (como con valor >= 1)
t = np.arange(0, T + t_n, t_n)
N_muestras = len(t)

X = np.zeros((num_realizaciones, N_muestras))

for r in range(0, num_realizaciones, 1):
    A = np.random.uniform(-2, -1)

    for k in range(0, N_muestras, 1):
        X[r, k] = np.exp(A * t[k])

plt.figure()

for r in range(0, num_realizaciones, 1):
    plt.plot(t, X[r, :], linewidth = 2)

plt.xlabel("t [s]")
plt.ylabel("X(t)")
plt.title("Proceso X(t) = exp(A * t)")
plt.grid()
plt.show()
