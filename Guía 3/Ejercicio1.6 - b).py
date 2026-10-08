import numpy as np
import matplotlib.pyplot as plt

t_s = 0.01
lamb = 0.5

num_realizaciones = 10
t = np.arange(0, 10 + t_s, t_s)
N_muestras = len(t)

S = np.zeros(N_muestras)
N = np.zeros((num_realizaciones, N_muestras))


for r in range(0, num_realizaciones, 1):
    tiempo_eventos = []
    tiempo_acumulado = 0

    while(tiempo_acumulado <= 10):
        U = np.random.uniform(0, 1)
        T = -(1 / lamb) * np.log(U) 

        tiempo_acumulado += T

        if(tiempo_acumulado <= 10):
            tiempo_eventos.append(tiempo_acumulado)


    for k in range(0, N_muestras, 1):
        for tiempo_evento in tiempo_eventos:
            if (tiempo_evento <= t[k]):
                N[r, k] += 1


plt.figure()

for r in range(0, num_realizaciones, 1):
    plt.plot(t, N[r, :], linewidth = 2)

plt.xlabel("t [s]")
plt.ylabel("N(t)")
plt.title("Proceso Poisson")
plt.legend()
plt.grid()
plt.show()
