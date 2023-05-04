from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/prompt')

layout = dbc.Container(children=[
    dbc.Row(
        [
            dbc.Col([
                    html.Div(children='What are the benefits to knowning the story behind the production of a good, like the shirt on your back or the shoes on your feet?', 
                    style={'fontSize': 50, 'text-align': 'center'}),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        html.Div(dbc.Button('Add Response', id='responseButton', color='dark', href='/response', className="buttons"), style={'text-align': 'center'}),
                        html.Br(),
                        html.Div(dbc.Button('Respond to Others', id='commentButton', color='dark', href='/collection', className="buttons"), style={'text-align': 'center'})
                    ]),
                    
            ],
            style={'margin-top':"10%"})

        ],
        justify="center",
        align="center",
        className="h-50"
    )
    

],

)