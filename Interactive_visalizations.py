import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

df = pd.DataFrame({
    "x": [1,2,1,2],
    "y": [1,2,3,4],
    "customdata": [1,2,3,4],
    "fruit": ["apple", "apple", "orange", "orange"]
})

fig = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=20)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),
    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Hover Data**
                
                Mouse over value in the graph
            """),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns'),
        html.Div([
            dcc.Markdown("""
                **Click Data**
                
                Click on point in the graph
            """),
            html.Pre(id='click-data', style=styles['pre'])
        ], className='three columns'),
        html.Div([
            dcc.Markdown("""
                **Selection Data**
                
                Chose the lasso or retangle tool in the graph's menu
                bar and then select points in the graph.
                
                Note that if 'layout.clickmode = event+select', selection data also
                accumulates (or un-accumulates) selected data if you hold down the shift button while clicking
            """),
            html.Pre(id='selected-data', style=styles['pre']),
        ], className='three columns'),
        html.Div([
            dcc.Markdown("""
                **Zoom and Relayout Data**
                
                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph menu bar
                Clicking on legend items will also fire this event
            """),
            html.Pre(id='relayout-data', style=styles['pre'])
        ], className='three columns')
    ])
])

# Hover callback
@app.callback(
    Output('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')]
)
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)

# Click callback
@app.callback(
    Output('click-data', 'children'),
    [Input('basic-interactions', 'clickData')]
)
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)

# Selection callback
@app.callback(
    Output('selected-data', 'children'),
    [Input('basic-interactions', 'selectedData')]
)
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)

# Reload callback
@app.callback(
    Output('relayout-data', 'children'),
    [Input('basic-interactions', 'relayoutData')]
)
def display_relayout_data(relayoutData):
    if relayoutData:
        return json.dumps(relayoutData, indent=2)
    else:
        return "Hello"

if __name__ == '__main__':
    app.run_server(debug=True)