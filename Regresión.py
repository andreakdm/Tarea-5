import numpy as np
import matplotlib.pyplot as plt

# Tus datos
x = np.array([1, 2, 3, 5, 5])
y = np.array([0.5, 2, 2.9, 3.5, 4])

# Transforma x tomando el logaritmo natural
ln_x = np.log(x)

# Ajusta un modelo lineal usando polyfit
m, c = np.polyfit(ln_x, y, 1)

# Calculo de a y b a partir de m y c
a = 1 / m
b = -c / m

# Predice y para x = 2.6
x_new = 2.6
ln_x_new = np.log(x_new)
y_predicho = m * ln_x_new + c

# Grafica los datos y la línea de regresión
plt.scatter(ln_x, y, color='blue', label='Datos')
plt.plot(ln_x, m * ln_x + c, color='red', label='Regresión lineal')
plt.axvline(x=ln_x_new, color='green', linestyle='--', label='x = {:.4f}'.format(x_new))
plt.axhline(y=y_predicho, color='purple', linestyle='--', label='y = {:.4f}'.format(y_predicho))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión lineal después de la transformación')
plt.legend()  # Agrega la leyenda
plt.show()

print(f'Los valores estimados son a = {a} y b = {b}')
print(f'La predicción para x = {x_new} es y = {y_predicho}')
