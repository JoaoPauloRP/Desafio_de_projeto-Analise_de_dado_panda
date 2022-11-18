

Original file is located at
    https://colab.research.google.com/drive/1ybqYtXrtcBjr-pDYy2QzErm1Zs_M5zQb
"""

#Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#Criando o DataFrame
df = pd.read_excel("/AdventureWorks.xlsx")

df["Valor Venda"].sum()

df["lucro liquido unitario"]  = df["Preço Unitário"] - df["Custo Unitário"]

df["Lucro Liquido Total"] = df["lucro liquido unitario"] * df["Quantidade"]

round(df["Lucro Liquido Total"].sum(),2)

df.head(1)

df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

#Gráfico Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["Lucro Liquido Total"].sum().plot.pie(title="Lucro x Ano");

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro Liquido Total"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro Liquido");

df_2009.groupby("Marca")["Lucro Liquido Total"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro Liquido")
plt.xticks(rotation='horizontal');

df_2009.groupby("Classe")["Lucro Liquido Total"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro Liquido")
plt.xticks(rotation='horizontal');

#Histograma
plt.hist(df["Tempo_envio"]);

