#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:55:50 2020

@author: eve
"""

import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd 
from main import app
import json
import base64


df = pd.read_csv('data/wheels.csv')
fig =  px.scatter(df,x='wheels', y= 'color')
fig.update_traces(marker = {
                        'size': 12,
                        'color': 'red'
                        } )
#fig.update_layout(title = 'wheels and col', title_x=0.5)


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

layout = html.Div([
    html.H1("Want a gear"),
    html.Hr(),
    html.H2("Click on a red circle to choose a color and a number of wheels for your gear"),
    html.Hr(),
    html.Div([dcc.Graph(id = 'figure',figure= fig)], style={'width':'50%', "float":'left'}),
    html.Img(id='image', src='children', height=300, "float":'right')
    ])

@app.callback( Output('image', 'src'),
              [Input('figure', 'clickData')])
def update_output(clickData):
    print(clickData['points'][0])
    x = clickData['points'][0]['x']
    y = clickData['points'][0]['y']
    row=df[(df['color']==y) & (df['wheels']==x) ]
    print(row['image'].values[0])
    image = 'images/'+row['image'].values[0]
    print(image)
    encoded_image = encode_image(image)

    return encoded_image