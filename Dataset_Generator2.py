import numpy as np
import matplotlib.pyplot as plt

# Definir los tiempos
tiempo = np.linspace(0, 10, 1000)  # 10 segundos divididos en 1000 puntos de datos

# Crear el voltaje en función del tiempo
voltaje = np.ones_like(tiempo) * 12  # nivel constante de 12V

# Caída de voltaje de 12V a 10V en el segundo 3
indice_caída = np.where(tiempo >= 3)[0][0]
voltaje[indice_caída:] -= np.interp(tiempo[indice_caída:], [3, 3.25], [0, 2])  # Caída lineal en 0.25 segundos

# Oscilaciones entre 9.7V y 10.2V después de 3.25 segundos
indice_oscilaciones = np.where(tiempo >= 3.25)[0][0]
voltaje[indice_oscilaciones:] = np.sin(10 * np.pi * tiempo[indice_oscilaciones:]) * 0.25 + 9.95  # Oscilaciones sinusoidales

# Aumento repentino a 14V después de 5 segundos
indice_aumento = np.where(tiempo >= 5)[0][0]
voltaje[indice_aumento:] += np.interp(tiempo[indice_aumento:], [5, 7], [0, 2])  # Aumento lineal en 2 segundos

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(tiempo, voltaje, color='blue')
plt.title('Gráfico de Nivel de Voltaje')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.grid(True)
plt.show()
