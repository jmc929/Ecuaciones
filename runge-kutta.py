import numpy as np

# Definir la función que representa la EDO
def f(x, y):
    return x**2 - 3*y 

# Método de Runge-Kutta de cuarto orden
def runge_kutta_4(f, x0, y0, h, x_end):
    n = int((x_end - x0) / h)  # Número de puntos
    x = np.linspace(x0, x_end, n+1)  # Puntos de x
    y = np.zeros(n+1)  # Arreglo para almacenar valores de y
    y[0] = y0  # Condición inicial

    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + k1/2)
        k3 = f(x[i] + h/2, y[i] + h/2 * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i+1] = y[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4) 
        
        # Imprimir resultados de cada iteración
        print(f"Iteración {i + 1}: x = {x[i]:.4f}, y = {y[i]:.4f}")
        print(f"    k1 = {k1:.4f}, k2 = {k2:.4f}, k3 = {k3:.4f}, k4 = {k4:.4f}, y = {y[i+1] :.4f}")
        

    return x, y

# Parámetros iniciales
x0 = 0
y0 = 1
h = 0.1  # Tamaño del paso
x_end = 4  # Valor final de x

# Llamar al método de Runge-Kutta
x, y = runge_kutta_4(f, x0, y0, h, x_end)

