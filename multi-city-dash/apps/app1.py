from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import dash_table_experiments as dt
from dash.dependencies import Input, Output, State, Event
import plotly

from app import app
from header import header
from flask_caching import Cache
import os
import copy

T_Household = pd.read_csv('./data/df_th.csv', index_col=0)
#T_Household = T_Household.iloc[0:4000]

total_rows=len(T_Household.axes[0])
total_cols=len(T_Household.axes[1])

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
# CACHE_CONFIG = {
#     # try 'filesystem' if you don't want to setup redis
#     'CACHE_TYPE': 'redis',
#     'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'localhost:6379')
# }
# cache = Cache()
# cache.init_app(app.server, config=CACHE_CONFIG)

layout = html.Div([
    header,
    html.H3('Datatable'),
    html.P('This table has ' + str(total_rows) + ' rows and ' + str(total_cols) + ' columns' \
    + ' - uncomment line #14 in app1.py for a full table'
        ),
    dt.DataTable(
        rows=T_Household.to_dict('records'),
        # optional - sets the order of columns
        #columns=sorted(T_Household.columns),
        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id='datatable-households'
        ),
        html.Div(id='selected-indexes'),
        dcc.Graph(
        id='graph-households'
        )
]) ######## END OF LAYOUT ########


#callbacks
@cache.memoize()
@app.callback(
    Output('datatable-households', 'selected_row_indices'),
    [Input('graph-households', 'clickData')],
    [State('datatable-households', 'selected_row_indices')])
def update_selected_row_indices(clickData, selected_row_indices):
    if clickData:
        for point in clickData['points']:
            if point['pointNumber'] in selected_row_indices:
                selected_row_indices.remove(point['pointNumber'])
            else:
                selected_row_indices.append(point['pointNumber'])
    return selected_row_indices

@app.callback(
    Output('graph-households', 'figure'),
    [Input('datatable-households', 'rows'),
     Input('datatable-households', 'selected_row_indices')])
def update_figure(rows, selected_row_indices):
    dff = pd.DataFrame(rows)
    fig = plotly.tools.make_subplots(
        rows=3, cols=1,
        subplot_titles=('Family households (families) - With own children of the householder under 18 years',
        'Family households (families)', 'Total households',),
        shared_xaxes=True)
    marker = {'color': ['#0074D9']*len(dff)}
    for i in (selected_row_indices or []):
        marker['color'][i] = '#FF851B'
    fig.append_trace({
        'x': dff['state'],
        'y': dff['02HC01_VC05'],
        'type': 'bar',
        'marker': marker
    }, 1, 1)
    fig.append_trace({
        'x': dff['state'],
        'y': dff['02HC01_VC04'],
        'type': 'bar',
        'marker': marker
    }, 2, 1)
    fig.append_trace({
        'x': dff['state'],
        'y': dff['02HC01_VC03'],
        'type': 'bar',
        'marker': marker
    }, 3, 1)
    fig['layout']['showlegend'] = False
    fig['layout']['height'] = 800
    fig['layout']['margin'] = {
        'l': 40,
        'r': 10,
        't': 60,
        'b': 200
    }
    fig['layout']['yaxis3']['type'] = 'log'
    return fig
