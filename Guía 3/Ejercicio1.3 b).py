import numpy as np
import matplotlib.pyplot as plt

num_realizaciones = 100
N = 200
n = np.arange(N)

X = np.zeros((num_realizaciones, N))

for r in range(0, num_realizaciones, 1):

    A = np.random.uniform(0, 1)
    B = np.random.uniform(0, 1)

    for k in range(0, N, 1):
        X[r, k] = A * k + B

mu_teo = n/2 + 0.5


plt.figure()

for r in range(0, num_realizaciones, 1):
    plt.plot(n, X[r, :])

plt.plot(n, mu_teo, color= "black" , linewidth= 3,label= "Media teorica")
plt.xlabel("n")
plt.ylabel("X(n)")
plt.title("Proceso X(n) = An + B")
plt.legend()
plt.grid()
plt.show()