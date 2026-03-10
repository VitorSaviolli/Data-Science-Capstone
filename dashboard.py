import dash
from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Dados de exemplo
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas = [12000, 15000, 13500, 17000, 16000, 19000]
despesas = [8000, 9500, 8700, 10200, 9800, 11000]

categorias = ["Produto A", "Produto B", "Produto C", "Produto D"]
participacao = [35, 25, 20, 20]

df_barras = pd.DataFrame({"Mês": meses, "Vendas": vendas, "Despesas": despesas})

# Gráficos
fig_linha = go.Figure()
fig_linha.add_trace(go.Scatter(x=meses, y=vendas, mode="lines+markers", name="Vendas", line=dict(color="#2196F3")))
fig_linha.add_trace(go.Scatter(x=meses, y=despesas, mode="lines+markers", name="Despesas", line=dict(color="#F44336")))
fig_linha.update_layout(title="Vendas vs Despesas", paper_bgcolor="#1e1e2f", plot_bgcolor="#1e1e2f",
                        font=dict(color="white"), legend=dict(bgcolor="#1e1e2f"))

fig_pizza = go.Figure(go.Pie(labels=categorias, values=participacao, hole=0.4))
fig_pizza.update_layout(title="Participação por Produto", paper_bgcolor="#1e1e2f",
                        font=dict(color="white"), legend=dict(bgcolor="#1e1e2f"))

fig_barras = px.bar(df_barras, x="Mês", y=["Vendas", "Despesas"], barmode="group",
                    color_discrete_sequence=["#2196F3", "#F44336"])
fig_barras.update_layout(title="Comparativo Mensal", paper_bgcolor="#1e1e2f", plot_bgcolor="#1e1e2f",
                         font=dict(color="white"), legend=dict(bgcolor="#1e1e2f"))

# App
app = dash.Dash(__name__)

app.layout = html.Div(style={"backgroundColor": "#12122a", "fontFamily": "Arial", "padding": "20px"}, children=[
    html.H1("Dashboard de Vendas", style={"textAlign": "center", "color": "white", "marginBottom": "30px"}),

    # KPIs
    html.Div(style={"display": "flex", "justifyContent": "space-around", "marginBottom": "30px"}, children=[
        html.Div(style={"backgroundColor": "#1e1e2f", "padding": "20px", "borderRadius": "10px", "width": "25%", "textAlign": "center"}, children=[
            html.H3("Total Vendas", style={"color": "#aaa", "margin": "0"}),
            html.H2(f"R$ {sum(vendas):,}", style={"color": "#2196F3", "margin": "10px 0 0 0"}),
        ]),
        html.Div(style={"backgroundColor": "#1e1e2f", "padding": "20px", "borderRadius": "10px", "width": "25%", "textAlign": "center"}, children=[
            html.H3("Total Despesas", style={"color": "#aaa", "margin": "0"}),
            html.H2(f"R$ {sum(despesas):,}", style={"color": "#F44336", "margin": "10px 0 0 0"}),
        ]),
        html.Div(style={"backgroundColor": "#1e1e2f", "padding": "20px", "borderRadius": "10px", "width": "25%", "textAlign": "center"}, children=[
            html.H3("Lucro", style={"color": "#aaa", "margin": "0"}),
            html.H2(f"R$ {sum(vendas) - sum(despesas):,}", style={"color": "#4CAF50", "margin": "10px 0 0 0"}),
        ]),
    ]),

    # Gráficos
    html.Div(style={"display": "flex", "gap": "20px", "marginBottom": "20px"}, children=[
        html.Div(style={"flex": "2"}, children=[dcc.Graph(figure=fig_linha)]),
        html.Div(style={"flex": "1"}, children=[dcc.Graph(figure=fig_pizza)]),
    ]),

    html.Div(children=[dcc.Graph(figure=fig_barras)]),
])

if __name__ == "__main__":
    app.run(debug=True)
