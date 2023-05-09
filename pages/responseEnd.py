from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/responseEnd')

layout = dbc.Container(children=[
        dbc.Row(
            dbc.Col(children='Thank you for adding.'), 
            style={'margin-top': '10%'}
        ),
        dbc.Row(
            dbc.Col(children='Find your response on the screen!'), 
        ),
        html.Br(),
        dbc.Row([
            html.Div(dbc.Button('Return', id='commentendButton', href='/',color="dark"), style={'text-align': 'center'})
        ]),

    ],
    style={'fontSize': 50, 'text-align': 'center'}
)