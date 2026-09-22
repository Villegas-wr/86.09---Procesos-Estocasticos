import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


####################################################################################################

# PCA - REDUCIR DIMENSIÓN

####################################################################################################

img_path = "img_01.jpg"     # Imagen de camellos
K = 30                      # 1 <= K <= 64  K = cantidad de componentes a conservar

# Cargar imagen y pasar a gris
img = Image.open(img_path).convert("L")
img = np.array(img)

# Truncar a múltiplos de 8 (para obtener un número entero de bloques)
h, w = img.shape
h_new = (h // 8) * 8
w_new = (w // 8) * 8
img = img[:h_new, :w_new]


# Cada matriz 8x8 es un bloque de 64 pixeles y se busca aplanar ese bloque a un vector que sea tomado como realizaciones del vector aleatorio X_vec
bloque = []
X_vec = []

for i in range (0, h_new, 8):               # Avanza de forma vertical en múltiplos de 8
    for j in range (0, w_new, 8):           # Avanza de forma horizontal en múltiplos de 8
        bloque = img[i:i+8, j:j+8]
        vec =  bloque.reshape(64)           # Aplana la matriz 8x8 a un subvector 64x1 de realizaciones
        X_vec.append(vec)

X_vec = np.array(X_vec)                     # dim (h_new/8  * w_new/8, 64)              


u_X = np.mean(X_vec, axis=0)                # Media de vector aleatorio
Cx = np.cov((X_vec - u_X), rowvar=False)    # Matriz de covarianza 64x64

auto_valores, auto_vectores = np.linalg.eigh(Cx)    # Devuelve los autovalores de menor a mayor

auto_valores = auto_valores[::-1]           # Reordeno los autovalores y autovectores de mayor a menor
auto_vectores = auto_vectores[:,::-1]

# P_K consiste en una matriz de todos los vectores a una dimensión de K componentes principales
P_K = auto_vectores[:,:K]                   # dim(64, K)
Y_vec = (X_vec - u_X) @  P_K                # De la forma en que construí X_vec no es necesario la transpuesta de P_K (observar las dimensiones)



####################################################################################################

# PCA - RECONSTRUCCIÓN DE LA IMAGEN

####################################################################################################

X_rec_centrada = Y_vec @ P_K.T             # X_reconstruida no es lo mismo que X_vec porque (si se usa K distinto de 64) en el proceso se perdió información
X_rec = X_rec_centrada + u_X

img_rec = np.zeros((h_new, w_new))
index = 0

for i in range(0, h_new, 8):               # Camino inverso de la compresión
    for j in range(0, w_new, 8):
        bloque_rec = X_rec[index].reshape(8,8)
        img_rec[i:i+8, j:j+8] = bloque_rec
        index += 1


####################################################################################################

# GRAFICO DE RESULTADOS

####################################################################################################

#Comparo la imagen original con la recostruida (en escala de grises)

fig, ax = plt.subplots(1, 2, figsize = (12, 5))

# Imagen original
ax[0].imshow(img, cmap = 'gray')
ax[0].set_title("Imagen original")
ax[0].axis('Off')

# Imagen reconstruida
ax[1].imshow(img_rec, cmap = 'gray')
ax[1].set_title(f"Imagen reconstruida con K = {K}")
ax[1].axis('Off')

plt.tight_layout()
plt.show()

print(f"\nLa cantidad de componentes usadas para la compresión es {K}")
print("\nLa elección de K viene de la mano con la información que uno esta dispuesto a perder, " \
"con cuantos autovectores y autovalores conservas en el proceso de compresión a reconstrucción." \
"Cuando se elige un valor bajo de K = mayor compresión implicando que la reconstrucción sea de mala calidad (imagen pixeleada), mientras que con mayor K = menor compresión dejando una imagen de mejor calidad (similar a la original)")
print("\nEn la PAC se almancena aproximadamente (N*K + 64*K + 64)/64*N porque se tiene N bloques que almacenan 64*N valores, siendo también que Y_vec, P_K y u_X almacenan N*K, 64*K y 64 valores, respectivamente." \
"Pero como los valores de P_K y u_X son pequeños se puede hacer una aproximación de K/64 de lo almacenado.")
