from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import sqlite3
import time

buttonClicked = "0"

sql_path = "/home/amyni/cms.636/data/collection.db"
def insertRow(text, likes, name, year):
    conn = sqlite3.connect(sql_path)
    cursor = conn.cursor()
    sql = '''
            INSERT INTO collection 
            (id, response, likes, name, year)
            VALUES (?,?,?,?,?);
          '''
    cursor.execute(''' SELECT COUNT(id) FROM collection; ''')
    cursor.execute(sql, (time.time() , text, likes, name, year))
    conn.commit()
    cursor.close()

    conn.close()

def getTop9():
    conn = sqlite3.connect(sql_path)
    cursor = conn.cursor()
    sql = '''
            SELECT * FROM collection 
            ORDER BY id DESC
            LIMIT 9;
          ''' 
    cursor.execute(sql)
    data = cursor.fetchall()

    return data

def getCards():
    data = getTop9()
    cards = []
    i = 0
    for response in data:
        card = dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.P(response[1], style={'textAlign': 'center'}),
                    html.P(response[3], style={'textAlign': 'right'}),
                    html.Div(dbc.Button('comment', id='commentButton' + str(i), href='/comment' + str(i),), style={'text-align': 'center'}),
                ])
            )
        )
        #cards[i%3].append(card)
        cards.append(card)
        i += 1
    return cards

def getButtonClicked():
    return buttonClicked

def updateButtonClicked(i):
    buttonClicked = int(i.replace("commentButton", "").replace(".n_clicks", ""))
    #print(buttonClicked)
