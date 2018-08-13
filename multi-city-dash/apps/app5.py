from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd

from app import app, data
from header import header
import os
from flask_caching import Cache

df = data
df = df.sort_values(['02HC01_VC03'])

####### cache locally
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

####### cache with redis
# CACHE_CONFIG = {
#     # try 'filesystem' if you don't want to setup redis
#     'CACHE_TYPE': 'redis',
#     'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'localhost:6379')
# }
# cache = Cache()
# cache.init_app(app.server, config=CACHE_CONFIG)

layout = html.Div([
            header,
            html.Div([
                    html.Div([
                    dcc.Dropdown(id='cities',
                                 placeholder='Cities',
                                 multi=True,
                                 value=tuple(),
                                 options=[{'label': c, 'value': c}
                                              for c in sorted(df['city'].unique())]),
                        ], style={'width': '35%', 'display': 'inline-block'}),
                    html.Div([
                            dcc.Dropdown(id='states',
                                         placeholder='States',
                                         value='',
                                         options=[{'label': r, 'value': r}
                                                  for r in sorted(df['state'].unique())]),
                        ], style={'width': '35%', 'display': 'inline-block'}),



                        ], style={'margin-left': '25%'}),
            html.Div([
                dcc.Graph(id='th_scatter',
                          config={'displayModeBar': False})

                        ])
])
# callbacks
@cache.memoize()
@app.callback(Output('th_scatter', 'figure'),
             [Input('cities', 'value'), Input('states', 'value')])
def color_city_and_states(cities, states):
    df_cities = df[df['city'].isin(cities)]
    df_states = df[df['state'] == states]
    return {'data': [go.Scatter(x=df['city'],
                                y=df[col],
                                mode='markers',
                                showlegend=True,
                                name=col)
                     for col in ['02HC01_VC03']] +

                    [go.Scatter(x=df_states['state'],
                                y=df_states[col],
                                mode='markers',
                                showlegend=False,
                                hoverinfo='x+text',
                                hovertext=df_states['state'],
                                marker={'color': '#000000', 'size': 10},
                                )
                     for col in ['02HC01_VC03']] +

                    [go.Scatter(x=[df_cities[df_cities['city'] == city]['city'].iloc[0] for i in range(3)],
                                y=df_cities[df_cities['city'] == city][['02HC01_VC03']].iloc[0],
                                mode='markers',
                                name=city,
                                marker={'size': 11, 'line': {'color': '#000000', 'width': 1}})
                     for city in cities],

           'layout': go.Layout(title=('Total Households - ' + ', '.join(cities)) +
                                     ('' if not states else '  (' + ',  '.join([states]) + ' Cities Highlighted)'),
                               height=650,
                               margin={'r': 0, 't': 70, 'b': 70, 'l': 40},
                               titlefont={'size': 22},
                               font={'family': 'Palatino'},
                               legend={'orientation': 'h', 'font': {'size': 18}, 'xanchor': 'center', 'x': 0.5},
                               xaxis={'showticklabels': False},
                               plot_bgcolor='',
                               paper_bgcolor='')}
