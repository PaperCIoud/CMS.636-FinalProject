from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/responseEnd')

layout = html.Div(children=[
    html.Div(children='Thank you for adding. Find your response on the wall!', 
             style={'fontSize': 50, 'text-align': 'center'}),
    html.Br(),
    html.Div([
        html.Div(dbc.Button('Share', id='responseButton', href='/',), style={'text-align': 'center'}),
        html.Br(),
        html.Div(dbc.Button('Return', id='commentButton', href='/',), style={'text-align': 'center'})
    ]),

])