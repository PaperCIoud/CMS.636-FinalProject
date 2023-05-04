from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import sqlite3
import time
import os

buttonClicked = "0"
current = os.getcwd()
collection_path = current + "/data/collection.db"
comment_path = current + "/data/comments.db"
def insertRow(text, likes, name, year):
    conn = sqlite3.connect(collection_path)
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
    conn = sqlite3.connect(collection_path)
    cursor = conn.cursor()
    sql = '''
            SELECT * FROM collection 
            ORDER BY id DESC
            LIMIT 9;
          ''' 
    cursor.execute(sql)
    data = cursor.fetchall()

    return data

def addComment(response, comment):
    conn = sqlite3.connect(comment_path)
    cursor = conn.cursor()
    sql = '''
            INSERT INTO comments
            (response, comment, time)
            VALUES (?,?,?);
          '''
    cursor.execute(sql, (response, comment, time.time()))
    conn.commit()
    cursor.close()

    conn.close()

def getComments(response):
    conn = sqlite3.connect(comment_path)
    cursor = conn.cursor()
    sql = '''
            SELECT * FROM comments
            WHERE response IS ?
            ORDER BY time DESC
            LIMIT 3;
          ''' 
    cursor.execute(sql, (response,))
    data = cursor.fetchall()

    return data

def getLikes(response):
    conn = sqlite3.connect(collection_path)
    cursor = conn.cursor()
    sql = '''
            SELECT likes FROM collection
            WHERE response IS ?
            ORDER BY id DESC
            LIMIT 1;
          ''' 
    cursor.execute(sql, (response,))
    data = cursor.fetchall()

    return data

def updateLikes(response, newLikes):
    conn = sqlite3.connect(collection_path)
    cursor = conn.cursor()
    sql = '''
            UPDATE collection
            SET likes = ?
            WHERE response IS ?
            LIMIT 1
          ''' 
    cursor.execute(sql, (newLikes, response))
    conn.commit()
    cursor.close()

    conn.close()


def getButtonClicked():
    return buttonClicked

def updateButtonClicked(i):
    buttonClicked = int(i.replace("commentButton", "").replace(".n_clicks", ""))
    #print(buttonClicked)
