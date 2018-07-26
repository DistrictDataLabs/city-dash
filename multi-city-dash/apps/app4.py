from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd

from app import app
from header import header

df = pd.read_csv('./data/df_th.csv', index_col=0).groupby(["state"], as_index=False).sum()
new_cols = ['state', '02HC01_VC03', '02HC01_VC04', '02HC01_VC05']
df = df[new_cols]
for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
             [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

df['text'] = df['state'] + '<br>' +\
    'Total Household '+df['02HC01_VC03']+' Family households (families) '+df['02HC01_VC04']+'<br>'+\
    'Family households (families) - With own children of the householder under 18 years '+df['02HC01_VC05']

layout = html.Div([
            header,
            html.H2('Choropleth Map - states layout'),
            dcc.Graph(
                id = 'states-choropleth',
                figure={
                    'data':[
                        go.Choropleth(
                            colorscale = scl,
                            autocolorscale = True,
                            locations = df['state'],
                            z = df['02HC01_VC03'].astype(float),
                            locationmode = 'USA-states',
                            text = df['text'],
                            marker = dict(
                                line = dict (
                                    color = 'rgb(255,255,255)',
                                    width = 2
                                ) ),
                            colorbar = dict(
                                title = "Total Household")
                        )
                    ],
                    'layout': go.Layout(
                        title = 'Total Household<br>(Hover for breakdown)',
                        geo = dict(
                            scope='usa',
                            projection=dict( type='albers usa' ),
                            showlakes = True,
                            lakecolor = 'rgb(255, 255, 255)')
                    )
                }
            )
]) ######## END OF LAYOUT ########
