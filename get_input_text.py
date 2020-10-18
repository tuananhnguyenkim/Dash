import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

# Css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Define app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Layout
app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Ha Noi'),
    dcc.Input(id='input-2-state', type='text', value='Ho Chi Minh'),
    html.Button(id='submit-button-state', n_clicks=0, children='SUBMIT'),
    html.Div(id='output'),
    html.Div(id='output2')
])

@app.callback(
    [Output('output', 'children'),
     Output('output2', 'children'),
     Output('input-1-state', 'value')],
    [Input('submit-button-state', 'n_clicks')],
    [State('input-1-state', 'value'),
     State('input-2-state', 'value')]
)
def update_output(n_clicks, input1, input2):
    result = u'''
    The Button has been pressed {} times,
    Input 1 is "{}",
    and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)
    if n_clicks == 0:
        return result, 'Please push submit button', input1
    else:
        return "Completed submit {} and {}". format(input1, input2), "Submited", ''

if __name__ == '__main__':
    app.run_server(debug=True)