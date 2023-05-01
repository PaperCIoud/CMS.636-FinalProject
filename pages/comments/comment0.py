from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from helpers import *

i = 0

dash.register_page(__name__, path='/comment'+str(i))

def getlayout():

    page = html.Div(children=[
        html.Div(children='Comment', style={'fontSize': 50, 'textAlign': 'center'}),
        html.Div(children= [getTop9()[i][1]], style={'fontSize': 50, 'textAlign': 'center'}, id="response"),

        
        dbc.Container (
        
        [
            html.Div([
                dbc.Label("Your Comment", html_for="comment-form"),
                dbc.Input(type="text", id="comment-form"+str(i))
            ]),
        ]),

        html.Div (dbc.Button('Submit', id='submitCommentButton'+str(i), href='/commentEnd',), style={'text-align': 'center'}),

        html.Div (id = 'COutput' + str(i), style={"visibility": False})

    ])

    return page


layout = getlayout


@dash.callback(
    Output('COutput' + str(i), 'children'),
    [Input('submitCommentButton' + str(i), 'n_clicks'), Input('response', 'children')],
    [State('comment-form'+str(i), 'value')]
)
def updateDatabase(n_clicks, response, comment):
    if n_clicks is not None:
        addComment(response[0], comment)
    return ""