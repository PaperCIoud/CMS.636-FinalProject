from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from helpers import *

i = 7

dash.register_page(__name__, path='/comment'+str(i))

def getlayout():

    page = html.Div(children=[
        html.Div(children='Comment', style={'fontSize': 50, 'textAlign': 'center'}),
        html.Div(children= getTop9()[i][1], style={'fontSize': 50, 'textAlign': 'center'}),

        
        dbc.Container (
        
        [
            html.Div([
                dbc.Label("Your Comment", html_for="comment-form"),
                dbc.Input(type="text", id="comment-form"+str(i))
            ]),
        ]),

        html.Div (dbc.Button('Submit', id='submitCommentButton'+str(i), href='/responseEnd',), style={'text-align': 'center'}),

        html.Div (id = 'dummyOutput', style={"visibility": False})

    ])

    return page



layout = getlayout