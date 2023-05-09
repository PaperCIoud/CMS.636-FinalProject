from dash import Dash, html, dcc, Output, Input, ctx, callback_context, State
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from helpers import *

dash.register_page(__name__, path='/collection', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

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


def getResponseCards():
    data = getTop9()
    cards = []
    i = 0
    for response in data:
        comments = getComments(response[1])
        cardContent = [dbc.CardBody([
                          html.P(response[1], style={'textAlign': 'center'}),
                          html.P(response[3], style={'textAlign': 'right'}),
                          dbc.Container([
                              dbc.Row([
                                  dbc.Col(
                                    [
                                        html.Div(
                                            dbc.Button(
                                                html.I(className="bi bi-chat-left-dots"),
                                                id='commentButton' + str(i), href='/comment',
                                                color = "light"
                                            ), 
                                            style={'text-align': 'center'}
                                        ),
                                    ],
                                    width=2
                                  ),
                                  dbc.Col(
                                    [
                                        html.Div(
                                            dbc.Button(
                                                [
                                                    html.I(className="bi bi-heart"), 
                                                    html.Sub(response[2], id="likeCount"+str(i))
                                                ], 
                                                id='likeButton' + str(i), 
                                                style={'text-align': 'center'},
                                                color="light"
                                            ),
                                        ),
                                    ],
                                    width=4
                                  )
                                ],
                                justify="end"
                              )
                              
                          ]) , 
                          
                      ])]
        for x in comments:
            cardContent.append(dbc.CardFooter([html.P(x[1], style={'textAlign': 'center'})]))

        card = (
            dbc.Card(
                cardContent
            )
        )
        #cards[i%3].append(card)
        cards.append(card)
        i += 1
    return cards


layout = html.Div([
    html.Div(id="log", style={'display': 'none'}),
    dcc.Interval(id='refresh', interval=1000),
    html.Div(id='content', className="container"),
])

@dash.callback(Output('content', 'children'),
              Input('refresh', 'n_intervals'))
def display_layout(n):
    cards = getResponseCards()
    
    allCards = [dbc.Row(
                    [
                        dbc.Col(cards[0], width=4,),
                        dbc.Col(cards[1], width=4,),
                        dbc.Col(cards[2], width=4,)
                    ],
                    align="start",
                    #className="h-50",
                    style={'margin-top': '20px', 'margin-bottom': '10px'}
                ),
                dbc.Row(
                    [
                        dbc.Col(cards[3], width=4,),
                        dbc.Col(cards[4], width=4,),
                        dbc.Col(cards[5], width=4,),
                        
                    ],
                    align='center',
                    style={'margin-top': '20px', 'margin-bottom': '10px'}
                    #className="h-50"
                    #justify="evenly"
                ),
                dbc.Row(
                    [
                        dbc.Col(cards[6], width=4,),
                        dbc.Col(cards[7], width=4,),
                        dbc.Col(cards[8], width=4,),
                    ],
                    align='center',
                    style={'margin-top': '20px', 'margin-bottom': '10px'}
                    #className="h-50"
                    #justify="evenly"
                ),]
    
    page = dbc.Container(children=[
            
            
            dbc.Row([
                    dbc.Col(
                        html.Div(children='Gallery', style={'fontSize': 50, 'textAlign': 'Left'}),
                    ),
                    dbc.Col(
                        dbc.Button(
                                html.I(className="bi bi-house-door-fill", style={"font-size": "2rem"}), 
                                id='homeButton', href='/', color = "light"
                            ), 
                        style={'text-align': 'right',},
                    )
                ],
                align="center",
                className="h-50"
            ),
            dbc.Row(
                [
                    html.P("Add your response on the tablet below", style={'fontSize': 25, 'textAlign': 'Left'})
                ]
            ),

            *allCards
        
            
        ],
        fluid=True
        #style={"height":"auto"}
    )
    
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
def getResponseText(data):
    clicked = data.get("buttonClicked", 0)
    return getTop9()[clicked][1]


@dash.callback(Output("log", "children"), 
               [Input("likeButton"+str(i), "n_clicks") for i in range(9)],
               )
def func(*args):
    trigger = callback_context.triggered[0] 
    if(trigger["value"] is not None): 
        buttonClicked = int(trigger["prop_id"].replace("likeButton", "").replace(".n_clicks", ""))
        response = getTop9()[buttonClicked][1]
        current = getLikes(response)[0][0]
        updateLikes(response, current + 1)
        return current + 1


# for i in range(9):
#     @dash.callback(Output("likeCount" + str(i), "children"),
#                    [Input("likeButton"+str(i), "n_clicks")])
#     def updateLikeCount(n_clicks,):
#         if(n_clicks is not None):
#             print(i)
#             response = getTop9()[i][1]
#             current = getLikes(response)[0][0]
#             newCount = current + 1
#             updateLikes(response, newCount)
#             return newCount
