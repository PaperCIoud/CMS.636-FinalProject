from dash import Dash, html, dcc, Output, Input, callback_context, State
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from helpers import *

dash.register_page(__name__, path='/collection', suppress_callback_exceptions=True)

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
    html.Div(id="log", ),
    dcc.Interval(id='refresh', interval=2000),
    html.Div(id='content', className="container"),
])

@dash.callback(Output('content', 'children'),
              Input('refresh', 'n_intervals'))
def display_layout(n):
    cards = getResponseCards()
    
    page = html.Div(children=[
        html.Div(children='Collection', style={'fontSize': 50, 'textAlign': 'Left'}),
        html.Div(dbc.Button('home', id='homeButton', href='/',), style={'text-align': 'right'}),
        
        dbc.Container([
                dbc.Row(
                    [
                        dbc.Col(cards[0], width=4,),
                        dbc.Col(cards[1], width=4,),
                        dbc.Col(cards[2], width=4,)
                    ],
                    align="start",
                    className="h-50",
                ),
                dbc.Row(
                    [
                        dbc.Col(cards[3], width=4,),
                        dbc.Col(cards[4], width=4,),
                        dbc.Col(cards[5], width=4,),
                        
                    ],
                    align='center',
                    className="h-50"
                    #justify="evenly"
                ),
                dbc.Row(
                    [
                        dbc.Col(cards[6], width=4,),
                        dbc.Col(cards[7], width=4,),
                        dbc.Col(cards[8], width=4,),
                    ],
                    align='center',
                    className="h-50"
                    #justify="evenly"
                ),
            ],
            style={"height": "100vh"}
        )
        
    ])
    
    return page

@dash.callback(Output("buttonlog", "data"), 
               [Input("commentButton"+str(i), "n_clicks") for i in range(9)],
               )
def func(*args):
    trigger = callback_context.triggered[0] 
    if(trigger["value"] is not None): 
        buttonClicked = int(trigger["prop_id"].replace("commentButton", "").replace(".n_clicks", ""))
        data = {"buttonClicked": buttonClicked}
        return data
    
@dash.callback(
    Output('responseContent', 'children'),
    Input('buttonlog', 'data'),
)
def getComment(data):
    clicked = data.get("buttonClicked", 0)
    return getTop9()[clicked][1]
