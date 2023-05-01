# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import sys
import helpers

app = Dash(__name__, use_pages=True)

app.layout = html.Div(children=[
    dash.page_container,
    #html.H1(children='MuseConnects', style={'fontSize': 50, 'testAlign': 'center'}),

],
#style={'text-align' : 'center'}
)

if __name__ == '__main__':
    #print(dash.page_registry.values())
    #print(sys.path)
    app.run_server(debug=True)