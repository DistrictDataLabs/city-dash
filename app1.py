import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# API map key
mapbox_access_token = 'pk.eyJ1IjoiZXhiYWxkIiwiYSI6ImNqaGYyYWdhejE2ejQzY24ycm5ka3dvd3YifQ.P_nA6egJyCpBE58CacGikQ'

# df for data and meta files
df = pd.read_csv('./data/df.csv', low_memory=False)
features = [] # add columns from meta file

app = dash.Dash()

# Boostrap CSS to style app layout
app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})


# dash app layout
app.layout = html.Div([ # begining of most outer div

    html.Div([ # Title - Row
            html.H1(
                'City Intelligence Dashboard Project',
                style={'font-family': 'Helvetica',
                       "margin-top": "25",
                       "margin-bottom": "0"},
                className='eight columns',
            ),
            html.Img( # DDL image within the row
                src="https://static1.squarespace.com/static/55fdfa38e4b07a55be8680a4/t/55ff389ae4b0af0b2a73db12/1527626285600/?format=1500w",
                className='two columns',
                style={
                    'height': '19%',
                    'width': '19%',
                    'float': 'right',
                    'position': 'relative',
                    'padding-top': 20,
                    'padding-right': 0
                },
            ),
            html.P( # paragraph text under the title
                'Source: U.S. Census Bureau, 2012-2016 American Community Survey 5-Year Estimates',
                style={'font-family': 'Helvetica',
                       "font-size": "120%",
                       "width": "80%"},
                className='eight columns',
            )

        ],
        className='row'
    ),
    # div return def update_text
    html.Div([
        html.P( # paragraph text under the title
            'Hover over a map',
            style={'font-family': 'Helvetica',
                   "font-size": "40%",
                   "width": "80%"},
            className='row',
        ),
        html.Div(id='some-text',title='Hover on Map',className='row') # FIX title
    ]),
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
    ],className = "nine columns"),

]) # end of most outer div

#callbacks
@app.callback(
    Output('some-text', 'children'),
    [Input('map', 'hoverData')]
)

# function for map hover
def update_text(hoverData):
    s = df[df['Unnamed: 0'] == hoverData['points'][0]['customdata']]
    return html.H5(
        '{}, {} | {} County, {} zipcode | {} Total Households'.format(
            s.iloc[0]['city'],
            s.iloc[0]['state'],
            s.iloc[0]['county'],
            s.iloc[0]['zipcode'],
            s.iloc[0]['02HC01_VC03']
        )
    )



# run the app server
if __name__ == '__main__':
    app.run_server(debug=True)
