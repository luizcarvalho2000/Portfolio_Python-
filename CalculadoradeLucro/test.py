import matplotlib.pyplot as plt

# criando alguns dados de amostra
x = ['A', 'B', 'C', 'D']
y = [10, 20, 30, 40]

# Criando o gráfico de barras

plt.bar(x, y)

# adiciona o símbolo do dólar como anotação de texto em cada barra
for i, v in enumerate(y):
    plt.text(i, v + 1, '${}'.format(v), ha='center', fontweight='bold')

# criando o título e os rótulos dos eixos
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores ($)')

plt.show()
