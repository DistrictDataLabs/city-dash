import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

mapbox_access_token = 'pk.eyJ1IjoiZXhiYWxkIiwiYSI6ImNqaGYyYWdhejE2ejQzY24ycm5ka3dvd3YifQ.P_nA6egJyCpBE58CacGikQ'

app = dash.Dash()

# df for data and meta files
df = pd.read_csv('./data/df.csv', low_memory=False)
features = [] # add columns from meta file

app.layout = html.Div([ # most outer div
                html.Div([ # div for title and text below it
                    html.H1('Cencus Data Map'),
                    html.H4('This is a dashboard'),
                    html.Div(id='some-text'),
                ]),
                html.Div([ # div for 1st dropdown
                html.H6('select X axis'),
                    dcc.Dropdown(id='xaxis',
                                options=[{'label': i, 'value': i} for i in features],
                                value='') # add default value
                                ],style={'width':'48%','display':'inline-block'}),
                html.Div([ # div for 2nd dropdown
                html.H6('select Y axis'),
                    dcc.Dropdown(id='xaxis',
                                options=[{'label': i, 'value': i} for i in features],
                                value='') # add default value
                                ],style={'width':'48%','display':'inline-block'}),

                html.Div([ # div for map graph
                    dcc.Graph(id='map', figure={
                        'data':[{
                            'lat': df['latitude'],
                            'lon': df['longitude'],
                            'marker': {
                                'color': '#59C3C3', #df['state'],
                                'size': 8,
                                'opacity': 0.4
                        },
                        'customdata': df['Unnamed: 0'],
                        'type': 'scattermapbox'
                        }],
                        'layout':{
                            'mapbox': {
                                'accesstoken': mapbox_access_token
                        },
                        'hovermode': 'closest',
                        'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}}
                    })
                ],style={'width':'48%','display':'inline-block'}),

                html.Div([ # div for a scatter graph
                dcc.Graph(id='scatter',
                figure={
                    'data': [
                        go.Scatter(
                            x = df['02HC01_VC03'],
                            y = df['02HC01_VC21'],
                            dy = 1,
                            mode = 'markers',
                            marker = {
                                'size': 12,
                                'color': 'rgb(51,204,153)',
                                'line': {'width': 2}
                                }
                        )
                    ],
                    'layout': go.Layout(
                        title = 'Total Households by Average size',
                        xaxis = {'title': 'Total Households '},
                        yaxis = {'title': 'Average size','nticks':3},
                        hovermode='closest'
                    )
                })
                ],style={'width':'38%','display':'inline-block'}),







])

@app.callback(
    Output('some-text', 'children'),
    [Input('map', 'hoverData')]
)

# function for map
def update_text(hoverData):
    s = df[df['Unnamed: 0'] == hoverData['points'][0]['customdata']]
    return html.H5(
        '{}, {} | {} County, {} zipcode'.format(
            s.iloc[0]['city'],
            s.iloc[0]['state'],
            s.iloc[0]['county'],
            s.iloc[0]['zipcode']
        )
    )

# can add different css here
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# run the app server
if __name__ == '__main__':
    app.run_server(debug=True)
