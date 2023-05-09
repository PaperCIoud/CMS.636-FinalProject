from dash import Dash, html, dcc, Output, Input, State
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from helpers import *

dash.register_page(__name__, path='/comment')


def getlayout(): 
    page = dbc.Container(children=[
                dbc.Row([
                        dbc.Col(
                            dbc.Button(
                                    html.I(className="bi bi-house-door-fill", style={"font-size": "2rem"}), 
                                    id='homeButton', href='/', color = "light"
                                ), 
                            style={'text-align': 'right',},
                        )
                    ],
                ),
                dbc.Row(
                    dbc.Col(
                        "",
                        id='responseContent'
                    ),
                    style={'fontSize': 50, 'textAlign': 'center','margin-top': '10%'}, 
                ),

                dbc.Row ([
                    dbc.Label("Your Comment", html_for="comment-form"),
                    dbc.Textarea(id="comment-form", rows=5, style={"border":"2px solid black"})
                ], style={'margin-top': '5%'}),
                dbc.Row (
                    html.Div (dbc.Button('Submit', id='submitCommentButton', href='/commentEnd', color="dark"), style={'text-align': 'center'}),
                    style={'margin-top': '5%',}
                ),
            
                html.Div (id = 'COutput', style={"visibility": False})

            ],
            
        )
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