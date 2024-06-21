import matplotlib.pyplot as plt

# Dane
wiek = [20, 30, 40, 50, 60, 70]
czytelnicy = [5, 20, 30, 20, 15, 10]
skumulowani_czytelnicy = [sum(czytelnicy[:i+1]) for i in range(len(czytelnicy))]
procenty = [x/100 for x in skumulowani_czytelnicy]

# Wykres dystrybuanty
plt.step(wiek, procenty, where='post', label='Dystrybuanta F(x)')
plt.scatter(wiek, procenty, color='red')

# Adnotacje
for i, txt in enumerate(procenty):
    plt.annotate(f"{txt:.2f}", (wiek[i], procenty[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.title('Dystrybuanta rozkładu wieku czytelników POLITYKI')
plt.xlabel('Wiek (lata)')
plt.ylabel('F(x)')
plt.grid(True)
plt.legend()
plt.show()
