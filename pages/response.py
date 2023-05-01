from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import sys
import time
sys.path.append("/pages")
import helpers

dash.register_page(__name__, path='/response')

layout = html.Div(children=[
    #html.Div(children='Response', style={'fontSize': 50, 'textAlign': 'center'}),

    

    dbc.Container (
    
    [
        html.Div([
            dbc.Label("Response", html_for="response-form"),
            dbc.Input(type="text", id="response-form")
        ]),

        html.Div([
            dbc.Label("Name", html_for="name-form"),
            dbc.Input(type="text", id="name-form")
        ]),

        html.Div([
            dbc.Label("Class Year", html_for="year-form"),
            dbc.Input(type="text", id="year-form")
        ])
    ]),

    html.Div (dbc.Button('Submit', id='submitButton', href='/responseEnd',), style={'text-align': 'center'}),

    html.Div (id = 'dummyOutput', style={"visibility": False})

])

@dash.callback(
    Output('dummyOutput', 'children'),
    Input('submitButton', 'n_clicks'),
    [State('response-form', 'value'),
    State('name-form', 'value'),
    State('year-form', 'value'),]
)
def updateDatabase(n_clicks, v1, v2, v3):
    if n_clicks is not None:
        helpers.insertRow(v1, 0, v2, v3)
    return ""