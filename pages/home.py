from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.Div(children='Home', style={'fontSize': 50, 'textAlign': 'center'}),

    html.Div(
        dbc.Button('next', id='nextButton', href='/prompt', color='primary', className="home_next"), 
        
    ),

])