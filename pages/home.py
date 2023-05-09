from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
        dbc.Row([
                dbc.Col([
                    html.Img(src="../assets/home.PNG", style={'height':'100vh', 'width':'60vh', "border": "3px", "box-sizing": "border-box"}, )
                ]),
                dbc.Col([
                    html.Img(src="../assets/logo.PNG", className="mit_image")
                ]),

                dbc.Col([
                    html.Div(children='Tracing Threads', style={'fontSize': 100, 'textAlign': 'center'}, className="home_text"),

                    html.Div(
                        dbc.Button('Enter Here', id='nextButton', href='/prompt', color='dark', className="home_next"), 
                    ),
                ],
                
                )

            ],
            className="g-0",
        )
    ],
    style={"overflow-x": "clip", "overflow-y": "clip","overflow": "hidden", "margin": 0, "padding": 0}
    )