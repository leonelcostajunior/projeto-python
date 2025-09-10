import pandas as pd

import plotly.express as px

tabela = pd.read_csv("vendas_distribuicao.csv")

grafico = px.sunburst(
    tabela,
    path=["Continente", "Pais"],
    values="Vendas (Milhões)",  # nome exato da coluna
    color="Continente",
    title="Divisão de Vendas Globais"
)

grafico.show(renderer="browser")
