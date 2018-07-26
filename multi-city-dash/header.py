from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

header = html.Div([
            html.Div(className='row',
                     style={'backgroundColor': '#f9e2be4f',
                            'color':'black', 'padding': 10},
                     children=[html.Div(className='nine columns',
                                        children=[
                                            html.H1("City Intelligence Dashboard Project",
                                                    style={'paddingBottom':0, 'font-weight':'bold'}),
                                            html.H6("Source: U.S. Census Bureau, 2012-2016 American Community Survey 5-Year Estimates",
                                                    style={'paddingTop':0, 'paddingBottom':0, 'font-size':'100%'}),
                                            # html.P(children=[html.A('GitHub',
                                            #                          href='https://github.com/DistrictDataLabs/sage',
                                            #                          style={'color': 'black', 'textAlign': 'right'})])
                                        ]),
                                html.Div(className='three columns',
                                         style={'float': 'right', 'paddingLeft': 20, 'padding-top': 10},
                                         children=[
                                            html.Img(src='https://static1.squarespace.com/static/55fdfa38e4b07a55be8680a4/t/55ff389ae4b0af0b2a73db12/1531951609241/?format=1500w',
                                                     style={'maxWidth':'100%'}),
                                ])
            ]),
                html.Div([
                    html.P('switch between apps',
                        style={'position': 'absolute',
                                'background-color': '#f9f9f9c7',
                                'align-items': 'center',
                                'width': '100%',
                                'display': 'flex',
                                'justify-content': 'center',
                                })],className='container'),

                #links to apps
                html.Div([
                    html.Div([dcc.Link('Index', href='/')],className='three columns'),
                    html.Div([dcc.Link('App1', href='/apps/app1')],className='three columns'),
                    html.Div([dcc.Link('App2', href='/apps/app2')],className='three columns'),
                    html.Div([dcc.Link('App3', href='/apps/app3')],className='three columns')]
                ,className='container',style={'padding': 25, 'color':'#39536B'})
])
