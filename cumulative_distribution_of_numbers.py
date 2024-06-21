import matplotlib.pyplot as plt

# Dane
liczba_bledow = [0, 1, 2, 3, 4, 5]
liczba_kandydatek = [15, 18, 12, 3, 2, 1]
skumulowana_liczba_kandydatek = [sum(liczba_kandydatek[:i+1]) for i in range(len(liczba_kandydatek))]

# Wykres skumulowanego rozkładu liczebności
plt.step(liczba_bledow, skumulowana_liczba_kandydatek, where='post', label='Skumulowany rozkład liczebności')
plt.scatter(liczba_bledow, skumulowana_liczba_kandydatek, color='red')

# Adnotacje
for i, txt in enumerate(skumulowana_liczba_kandydatek):
    plt.annotate(f"{txt}", (liczba_bledow[i], skumulowana_liczba_kandydatek[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.title('Skumulowany rozkład liczebności liczby błędów')
plt.xlabel('Liczba błędów')
plt.ylabel('Skumulowana liczba kandydatek')
plt.grid(True)
plt.legend()
plt.show()
