from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

from app import app
from apps import app1, app2, app3
from index import layout
from header import header


app.title = 'This is a title'
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    # hidden table component to show table in other apps
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'})
])
index_page = layout

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return index_page
    elif pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/app2':
         return app2.layout
    elif pathname == '/apps/app3':
         return app3.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
