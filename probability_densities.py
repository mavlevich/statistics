import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametry rozkładu normalnego
mu = 80
sigma = 16

# Wartość X
x_value = 48

# Wykres gęstości prawdopodobieństwa
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Wykres
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Rozkład normalny N(80, 16)')
plt.fill_between(x, y, where=(x >= x_value), color='red', alpha=0.5, label='P(X > 48)')
plt.axvline(x=x_value, color='red', linestyle='--')
plt.title('Rozkład normalny N(80, 16) i prawdopodobieństwo P(X > 48)')
plt.xlabel('X')
plt.ylabel('Funkcja gęstości prawdopodobieństwa')
plt.legend()
plt.grid(True)
plt.show()
