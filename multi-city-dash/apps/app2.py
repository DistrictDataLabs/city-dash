from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd

from app import app
from header import header

df = pd.read_csv('./data/df_th.csv', low_memory=False)
# API map key
mapbox_access_token = 'pk.eyJ1IjoiZXhiYWxkIiwiYSI6ImNqaGYyYWdhejE2ejQzY24ycm5ka3dvd3YifQ.P_nA6egJyCpBE58CacGikQ'

layout = html.Div([
            header,
            html.Div([
            html.Div(html.H4(['Mouse over a point on map'],id='text-hover',className='row')),
            dcc.Graph(id='map', figure={
                'data':[{
                    'lat': df['latitude'],
                    'lon': df['longitude'],
                    'marker': {
                        'color': '#59C3C3', #df['state'],
                        'size': 8,
                        'opacity': 0.4
                },
                'customdata': df.index,
                'type': 'scattermapbox'
                }],
                'layout':{
                    'mapbox': {
                        'accesstoken': mapbox_access_token,
                        'bearing':0,
                        'center':{
                        'lat':38.72490,
                        'lon':-95.61446,
                        },
                        'pitch':0,
                        'zoom':2.5,
                        'style':'light'
                },
                'hovermode': 'closest',
                'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}}
            })]),

]) ######## END OF LAYOUT ########

#callbacks
@app.callback(
    Output('text-hover', 'children'),
    [Input('map', 'hoverData')]
)

# function for map hover
def update_text(hoverData):
    s = df[df.index == hoverData['points'][0]['customdata']]
    return html.Div(
        '{}, {} | {} County, {} zipcode | {} Total Households'.format(
            s.iloc[0]['city'],
            s.iloc[0]['state'],
            s.iloc[0]['county'],
            s.iloc[0]['zipcode'],
            s.iloc[0]['02HC01_VC03']
        )
    )
