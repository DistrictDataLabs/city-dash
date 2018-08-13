import dash
import os
import pandas as pd
from flask import send_from_directory

app = dash.Dash()
server = app.server
app.config.supress_callback_exceptions = True

# Add css (static and/or from url)
external_css = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    '/static/base.css'
]
for css in external_css:
    app.css.append_css({"external_url": css})

# Load data
data = pd.read_csv('./data/dfc.csv', index_col=0, low_memory=False)

@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)
