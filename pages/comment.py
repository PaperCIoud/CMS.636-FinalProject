from dash import Dash, html, dcc, Output, Input, State
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from helpers import *

dash.register_page(__name__, path='/comment')


def getlayout(): 
    page = html.Div(children=[
            html.Div(children='Comment', style={'fontSize': 50, 'textAlign': 'center'}),
            html.Div(children= "", style={'fontSize': 50, 'textAlign': 'center'}, id='responseContent'),

            dbc.Container (
        
        [
            html.Div([
                dbc.Label("Your Comment", html_for="comment-form"),
                dbc.Input(type="text", id="comment-form")
            ]),
        ]),

        html.Div (dbc.Button('Submit', id='submitCommentButton', href='/commentEnd',), style={'text-align': 'center'}),

        html.Div (id = 'COutput', style={"visibility": False})

        ])
    return page
    

layout = getlayout


@dash.callback(
    Output('COutput', 'children'),
    [Input('submitCommentButton', 'n_clicks'), Input('responseContent', 'children')],
    [State('comment-form', 'value')]
)
def updateDatabase(n_clicks, response, comment):
    if n_clicks is not None:
        addComment(response, comment)
    return ""