import numpy as np
import matplotlib.pyplot as plt

# Dane
x = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
y = np.array([400, 450, 600, 500, 550, 650, 700, 750, 800, 850])

# Obliczanie średnich wartości
x_mean = np.mean(x)
y_mean = np.mean(y)

# Obliczanie współczynnika nachylenia b
b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)

# Obliczanie współczynnika trendu a
a = y_mean - b * x_mean

# Wyznaczanie wartości przewidywanych
y_pred = a + b * x

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Dane rzeczywiste')
plt.plot(x, y_pred, color='red', label='Linia trendu')
plt.xlabel('Rok')
plt.ylabel('Liczba absolwentów')
plt.title('Liczba absolwentów w poszczególnych latach')
plt.legend()
plt.grid(True)
plt.show()

# Współczynniki
a, b
