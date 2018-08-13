from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd

from app import app
from header import header
#from flask_caching import Cache

#cache = app.cache

# API map key
mapbox_access_token = 'pk.eyJ1IjoiZXhiYWxkIiwiYSI6ImNqaGYyYWdhejE2ejQzY24ycm5ka3dvd3YifQ.P_nA6egJyCpBE58CacGikQ'

# Testing counties layout
layout = html.Div([
            header,
            html.H2('Choropleth Map - counties layout'),
            dcc.Graph(
                id = 'county-choropleth',
                figure={
                    'data':[
                        go.Scattermapbox(
                            lat=['45.5017'],
                            lon=['-73.5673'],
                            text = []
                            )
                    ],
                    'layout': go.Layout(
                        mapbox = dict(
                            layers = [
                                dict(
                                    sourcetype = 'geojson',
                                    source = 'https://raw.githubusercontent.com/python-visualization/folium/master/tests/us-counties.json',
                                    type = 'fill',
                                    color = '#59C3C3'
                                )
                            ],
                            accesstoken = mapbox_access_token,
                            style = 'light',
                            center=dict(
                                lat=38.72490,
                                lon=-95.61446,
                            ),
                            pitch=0,
                            zoom=2.5
                        )
                    )
                }
            )
]) ######## END OF LAYOUT ########
#@cache.memoize()
