from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/prompt')

layout = html.Div(children=[
    html.Div(children='What are the benefits to knowning the story behind the production of a good, like the shirt on your back or the shoes on your feet?', 
             style={'fontSize': 50, 'text-align': 'center'}),
    html.Br(),
    html.Div([
        html.Div(dbc.Button('Add Response', id='responseButton', href='/response',), style={'text-align': 'center'}),
        html.Br(),
        html.Div(dbc.Button('Respond to Others', id='commentButton', href='/collection',), style={'text-align': 'center'})
    ]),

])