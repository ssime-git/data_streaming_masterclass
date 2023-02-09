from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# première lecture
df = pd.read_csv("sentiment_scores.txt", names=["score"])

# création du graphique
fig = px.line(df["score"][-50:])

# présentation du dashboard
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='interval-graph',
        figure=fig
    ),
    dcc.Interval(
        id='interval-component',
        interval=3*1000,  # in milliseconds
        n_intervals=1
    )
],
                      style={
                          "background-color": "black",
                          "color": "white"
                      })


@app.callback(
    Output('interval-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_figure(_):
    
    # relecture du fichier un instant plus tard
    df = pd.read_csv("sentiment_scores.txt", names=["score"])
    df["color"] = "red"
    print(len(df))
    fig = px.line(df["score"][-50:])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)