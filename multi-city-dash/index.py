from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app
from header import header

layout = html.Div([
        header,
        html.Div([
            html.H3('City Intelligence Dashboard Project'),
            html.H4('Source: U.S. Census Bureau, 2012-2016 American Community Survey 5-Year Estimates'),
            html.P('The files containing the data are the ones whose filenames end with “ann.csv.” \
            Each file has a different set of metrics by zip code (demographic, economic, housing, etc.).\
            The rest of the files contain either metadata or other info about the data in the files.'),
            html.P('The main goal here is to be able to aggregate to a city level and display a mix of \
            interactive visualizations and natural language descriptions on a dashboard.')
            ])
        ])
