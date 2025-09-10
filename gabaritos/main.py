import pandas as pd
import plotly.express as px
import webbrowser
import os

# Caminho padrão do Chrome no Windows (ajuste se estiver em outro local)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

# Registrar o Chrome como navegador
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Dados de exemplo
tabela = pd.read_csv("vendas_distribuicao.csv")


# Criar gráfico Sunburst
grafico = px.sunburst(
    tabela,
    path=["Continente", "Pais"],
    values="Vendas (Milhões)",
    color="Continente",
    title="Divisão de Vendas Globais"
)

grafico.update_traces(textinfo="label+percent entry")

# Abrir diretamente no Chrome
grafico.show(renderer="chrome")
