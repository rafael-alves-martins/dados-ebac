# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.lineplot(x='dia', y='venda', data=df, marker='o', color='blue')
plt.title('Preço da Gasolina por Dia')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda')
plt.grid(True)

# Salvando o gráfico em um arquivo PNG
plt.savefig('gasolina.png')