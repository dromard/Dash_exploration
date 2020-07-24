# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:32:23 2020

@author: eve
"""



import pandas as pd
import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import numpy as np
from dash.dependencies import Output, Input, State
from pandas_datareader import tiingo
import pandas_datareader.data as web
import dash_bootstrap_components as dbc
from datetime import datetime, timedelta, date
from app import app

min_date_allowed=datetime(2017, 1,1)
max_date_allowed=datetime.now()- timedelta(days=2)
df =  tiingo.get_tiingo_symbols() 
df = df.dropna()
df['startDate'] = pd.to_datetime(df['startDate'])
df['endDate'] = pd.to_datetime(df['endDate'])
#symb =symb['ticker'].iloc[4309:].values


df = df[(df['startDate'] < min_date_allowed) & (df['endDate'] > max_date_allowed )]
symb =df['ticker'].values

API_TOKEN = 'd65139f94845e295c10bdcb614021a21c17f2326'
start_dt = min_date_allowed.date()
end_dt = max_date_allowed.date()
data = web.get_data_tiingo(['AA','AAAAX'],start= start_dt, end=end_dt, api_key=API_TOKEN)
data = data.reset_index()
data = data.rename(columns={ 'close':'price', 'symbol':'stock'})
fig = px.line(data, x='date', y ='price', color='stock')
fig.update_traces(mode="markers+lines")
fig.update_xaxes(showgrid=False, zeroline=True)

layout = html.Div([
                    html.H1("Stock Price App using Tingo API"),
                    html.Hr(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(children=dcc.Dropdown(
                                    id='StockType',
                                    options= [{'label': i, 'value': i} for i in symb],
                                    value=['AA','AAAAX'],
                                    multi=True)
                                   ),
                            dbc.Col(children=dcc.DatePickerRange(
                                        id='my-date-picker-range',
                                        min_date_allowed=min_date_allowed,
                                        max_date_allowed=max_date_allowed,
                                        start_date=start_dt,
                                        end_date=end_dt)
                                   ),
                            dbc.Col(children=html.Button(id='submit', n_clicks=0, children='Submit'))
                        ])
                    ]),
                    html.Hr(),
                    html.Div(id="graph_div",children = [
                        dcc.Graph(id = "graph", figure= fig)])
])

@app.callback(Output("graph_div", "children"),
              [Input('submit', 'n_clicks')],
              [State('StockType', 'value'),
              State('my-date-picker-range', 'start_date'),
              State('my-date-picker-range', 'end_date')])
def update_graph(n_clicks, val, start_date, end_date):
    start_date = date.fromisoformat(start_date)
    end_date = date.fromisoformat(end_date)
    try:
        data = web.get_data_tiingo(val,start= start_date, end=end_date, api_key=API_TOKEN)
    except:
        try:
            data = web.get_data_tiingo(val,start= min_date_allowed, end=max_date_allowed, api_key=API_TOKEN)
            data = df[(df['startDate'] < min_date_allowed) & (df['endDate'] > max_date_allowed )]
        except:
            return html.H2('The API Tiingo is down, restart later.\n See you') # full control over the error UI
    try:
        data = data.reset_index()
        data = data.rename(columns={ 'close':'price', 'symbol':'stock'})
        fig = px.line(data, x='date', y ='price', color='stock')
        fig.update_traces(mode="markers+lines")
        fig.update_xaxes(showgrid=False, zeroline=True)
        return dcc.Graph(id = "graph", figure= fig)
    except:
        return html.Div('The NB of API calls to IEX API have been exceeded, retry tomorrow or enter a new API IEX key') # full control over the error UI



