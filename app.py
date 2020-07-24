# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:46:42 2020

@author: eve
"""

import dash
import dash_auth
import dash_bootstrap_components as dbc


VALID_USERNAME_PASSWORD_PAIRS = {
    'Data': 'lovers'
}

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

server = app.server
