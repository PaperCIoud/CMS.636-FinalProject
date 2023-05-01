from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/commentEnd')

layout = html.Div(children=[
    html.Div(children='Thank you for adding. Find your comment on the wall!', 
             style={'fontSize': 50, 'text-align': 'center'}),
    html.Br(),
    html.Div([
        html.Div(dbc.Button('Return', id='commentToHomeButton', href='/prompt',), style={'text-align': 'center'})
    ]),

])