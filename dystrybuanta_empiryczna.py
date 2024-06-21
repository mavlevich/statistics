import matplotlib.pyplot as plt

# Dane
liczba_bledow = [0, 1, 2, 3, 4, 5]
liczba_kandydatek = [15, 18, 12, 3, 2, 1]
skumulowana_liczba_kandydatek = [sum(liczba_kandydatek[:i+1]) for i in range(len(liczba_kandydatek))]

# Dystrybuanta empiryczna
dystrybuanta_empiryczna = [x/51 for x in skumulowana_liczba_kandydatek]

# Wykres dystrybuanty empirycznej
plt.step(liczba_bledow, dystrybuanta_empiryczna, where='post', label='Dystrybuanta empiryczna')
plt.scatter(liczba_bledow, dystrybuanta_empiryczna, color='red')

# Adnotacje
for i, txt in enumerate(dystrybuanta_empiryczna):
    plt.annotate(f"{txt:.3f}", (liczba_bledow[i], dystrybuanta_empiryczna[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.title('Dystrybuanta empiryczna liczby błędów')
plt.xlabel('Liczba błędów')
plt.ylabel('F(x)')
plt.grid(True)
plt.legend()
plt.show()
