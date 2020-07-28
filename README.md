## Dash Exploration

In this repo I explore some functionalities of Dash: dash dropdown, dash date range selection, dash interaction with plots, dash authentification, dash navigations and multipages

I mainly use the following dash components:
* dash_bootstrap_components: used for Dash styling and navigation components
* dash_core_components as dcc: for dash elements
* dash_html_components as html: to deal with HTML components
* dash_auth: for authentifications
* dash.dependencies: to deal with Interactions with users (Input, Output, State)

It uses the server gunicorn.

# How TO
- install the requirements:
`pip install -r requirements.txt`
- launch with gunicorn
`gunicorn main:server --bind=127.0.0.1:8000`
- you can also deploy it on Heroku, the file `Procfile` needed for herju deployment is already available

# See in action
To access to the deployment of this repo with my Heroku account you need a login and a username, send me a mail to get it. Then follow this link:
https://dash-exploration.herokuapp.com/


