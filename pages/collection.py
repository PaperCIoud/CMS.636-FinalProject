from dash import Dash, html, dcc, Output, Input, callback_context
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

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Tab 1"),
        dbc.Tab(tab2_content, label="Tab 2"),
        dbc.Tab(
            "This tab's content is never seen", label="Tab 3", disabled=True
        ),
    ],
    active_tab="tab_0"
)



layout = html.Div([
    html.Div(id="log", ),
    dcc.Interval(id='refresh', interval=2000),
    html.Div(id='content', className="container"),
    # dbc.Tabs(
    #     [
    #         dbc.Tab(tab1_content, label="Tab 1", tab_id="tab_0"),
    #         dbc.Tab(tab2_content, label="Tab 2", tab_id="tab_1"),
    #         dbc.Tab(
    #             [dcc.Interval(id='refresh', interval=2000),
    #             html.Div(id='content', className="container")], 
    #             label="Tab 3", tab_id="tab_2"
    #         ),
    #     ],
    #     id="tab",
    # )
])

@dash.callback(Output('content', 'children'),
              Input('refresh', 'n_intervals'))
def display_layout(n):
    cards = getCards()
    
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
                    className="h-25",
                ),
                dbc.Row(
                    [
                        dbc.Col(cards[3], width=4,),
                        dbc.Col(cards[4], width=4,),
                        dbc.Col(cards[5], width=4,),
                        
                    ],
                    align='center',
                    className="h-25"
                    #justify="evenly"
                ),
                dbc.Row(
                    [
                        dbc.Col(cards[6], width=4,),
                        dbc.Col(cards[7], width=4,),
                        dbc.Col(cards[8], width=4,),
                    ],
                    align='center',
                    className="h-25"
                    #justify="evenly"
                ),
            ],
            style={"height": "100vh"}
        )
        
    ])
    
    return page

# @dash.callback(Output("tab", "active_tab"), 
#                [Input("commentButton"+str(i), "n_clicks") for i in range(9)],
#                )
# def func(*args):
    
#     trigger = callback_context.triggered[0] 
#     if(trigger["value"] is not None): 
#         buttonClicked = "tab_" + (trigger["prop_id"].replace("commentButton", "").replace(".n_clicks", ""))
#         print(buttonClicked)
#         return buttonClicked
