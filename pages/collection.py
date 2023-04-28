from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from helpers import *

dash.register_page(__name__, path='/collection')

# data = getTop9()
# print(data)
# cards = [[],[],[]]
# i = 0
# for response in data:
#     card = dbc.Col(
#         dbc.Card(
#             dbc.CardBody([
#                 html.P(response[1], style={'textAlign': 'center'}),
#                 html.P(response[3], style={'textAlign': 'right'})
#             ])
#         )
#     )
#     cards[i%3].append(card)




layout = html.Div([
    dcc.Interval(id='refresh', interval=2000),
    html.Div(id='content', className="container")
])

@dash.callback(Output('content', 'children'),
              Input('refresh', 'n_intervals'))
def display_layout(n):

    page = html.Div(children=[
    html.Div(children='Collection', style={'fontSize': 50, 'textAlign': 'Left'}),
    html.Div(dbc.Button('home', id='homeButton', href='/',), style={'text-align': 'right'}),

    dbc.Container([
            #dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(card, width=4,)
                        for card in row
                    ],
                    align="start",
                    className="h-75",
                )
                for row in getCards()
            # #),
            # #dbc.Container(
            #     dbc.Row(
            #         [
            #             dbc.Col(cards[3], width=4,),
            #             dbc.Col(cards[4], width=4,),
            #             dbc.Col(cards[5], width=4,),
                        
            #         ],
            #         align='center',
            #         className="h-25"
            #         #justify="evenly"
            #     ),
            # #),
            # #dbc.Container(
            #     dbc.Row(
            #         [
            #             dbc.Col(cards[6], width=4,),
            #             dbc.Col(cards[7], width=4,),
            #             dbc.Col(cards[8], width=4,),
            #         ],
            #         align='end',
            #         className="h-25"
            #         #justify="evenly"
            #     ),
            #),
            ],
            #fluid = True,
            style={"height": "90vh"}
        )
    ])
    return page