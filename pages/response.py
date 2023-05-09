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
            
            dbc.Row([
                    dbc.Label("Your Response", html_for="response-form"),
                    dbc.Textarea(id="response-form", rows=5, style={"border":"2px solid black"})
                ], 
                style={'margin-top': '10%'},
            ),
            html.Br(),
            dbc.Row([
                dbc.Label("Name (Optional!)", html_for="name-form"),
                dbc.Input(type="text", id="name-form", style={"border":"2px solid black"})
            ]),

            dbc.Row(
                html.Div (dbc.Button('Submit', id='submitButton', href='/responseEnd', color="dark"), style={'text-align': 'center'}),
                style={'margin-top': '5%',}
            )
        ],
        
    ),

    #html.Div (dbc.Button('Submit', id='submitButton', href='/responseEnd', color="dark"), style={'text-align': 'center'}),
    
    html.Div (id = 'dummyOutput', style={"visibility": False})

])

@dash.callback(
    Output('dummyOutput', 'children'),
    Input('submitButton', 'n_clicks'),
    [State('response-form', 'value'),
    State('name-form', 'value'),]
)
def updateDatabase(n_clicks, v1, v2):
    if n_clicks is not None:
        helpers.insertRow(v1, 0, v2, 0)
    return ""