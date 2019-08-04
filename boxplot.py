import matplotlib.pyplot as plt
import random

vetor = []

for i in range(100):
    numero_aleatorio = random.randint(0,80)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot Aleatório")
plt.show()
