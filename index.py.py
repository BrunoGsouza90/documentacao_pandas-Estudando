''' Esse estudo foi baseado na documentação oficial do pandas.
    https://pandas.pydata.org/docs/user_guide/10min.html '''


#   Importação das bibliotecas "pandas" e "numpy" que serão usadas nesse estudo.
import numpy as np
import pandas as pd

#   Cria uma tabela com duas colunas, sendo a de índice já pronta, e o que vai dentro da lista
#       são os dados que irão na coluna de dados.  
s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)
print('')

#   Gerador de números aleatórios para o uso na np.random.randn.
np.random.seed(42)

#   Criação de uma variável recebendo uma tabela de uma lista que vai receber uma data específica,
#       mostrando apartir dela um periodo específico da data em ordem crescente.
dates = pd.date_range("20240614", periods = 6)
print(dates)
print('')

#   Criação de uma tabela com mais de uma coluna de dados:
#       "np.ramdom.randn(6, 4)" = Serão gerados números de raio aleatórios em 6 linhas e 4 colunas.
#       "index=dates" = Os índices das linhas serão as datas armazenadas pelo gerador de datas
#           da linha 17.
#       "columns=list("ABCD")" = Os índices das colunas.
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
print('')

#   Criação de uma tabela com mais de uma coluna de dados criada manualmente:
#       "pd.Timestamp" = Vai gerar uma data específica igual para todas as colunas.
#       "pd.Series":
#           "1" = Número que será gerado.
#           "index=list(range(5))" = Gerador de 5 linhas 1 para cada número.
#           "dtype="float32" = Tipo de número flutuante "real".
#       "np.array":
#           "[3] * 5" = Criação de 5 números 3.
#           "dtype=int32" = Tipo de número inteiro.
#       "pd.Categorical" = Criação de strings.
#       "pd.Series":
#           "list(range(0,5))" = Gerador de 5 números em ordem crescente.
#           "index=list(range(5))" = Gerador de 5 linhas uma para cada número.
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(5)), dtype="float32"),
        "D": np.array([3] * 5, dtype="int32"),
        "E": pd.Categorical(["test", "train", "teste", "train", "trust"]),
        "F": "foo",
        "G": pd.Series(list(range(0,5)), index=list(range(5)), dtype="int"),
    }
)
print(df2)
print('')

#   Impressão do tipo de cada coluna da váriavel df2.
print(df2.dtypes)
print('')

#   Impressão das 5 primeiras linhas da tabela armazenada da variável df.
print(df.head(5))
print('')

#   Impressão das 3 últimas linhas apresentadas na tabela da variável df.
print(df.tail(3))
print('')

#   Impressão dos índices de linha da tabela.
print(df.index)
print('')

#   Impressão dos índices de coluna da tabela.
print(df.columns)
print('')

#   Impressão do conteúdo da tabela.
print(df.to_numpy())
print('')

#   Impressão do contéudo de cada linha da tabela.
print(df2.to_numpy())
print('')

#   Impressão de um resumo estatístico de cada linha da tabela.
print(df.describe())
print('')

#   Impressão da tabela virada, colocando os índices de linha como índices
#       de colunas, e índices de colunas como índices de lnha.
print(df.T)
print('')

#   Impressão da tabela em estilo MarkDown.
print(df2.to_markdown())
print('')

#   Impressão classificada por um eixo.
print(df.sort_index(axis=0, ascending=True))
print('')

#   Impressão classificada por valores.
print(df.sort_values(by= "B"))
print('')

#   Impressão de uma coluna específica.
print(df2["D"])
print('')

#   Impressão de linhas específicas.
print(df2[0:3])
print('')

#   Impressão de uma linha específica.
print(df2.loc[[2]])
print('')

#   Impressão de colunas específicas.
print(df2.loc[:, ["A","B"]])
print('')

#   Impressão de linhas e colunas específicas.
print(df2.loc["1":"3", ["A","B"]])
print('')

#   Impressão de um dado específico da tabela em sua determinada posição.
print(df.loc[dates[0], "A"])
print(df.at[dates[0], "A"])
print('')