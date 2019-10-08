# para empezar, sólo necesitan estos imports
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# crean la app y le mandan los parámetros que consideren necesarios
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# le dicen a la app cuál va a ser el layout. Es HTML + Plotly
app.layout = html.Div(children=[
    html.H1(children='Hola Dash desde Scipy Latam'),

    html.Div(children='''
        Dash: A web application framework for Python. Los Dash Core Components no son
        HTML puro. Estos son generando combinando JS, CSS y HTML + ReactJS. 

        Dash es declarativo, sus componentes se definen a partir de los arguementos.
    '''),
    # Esta gramática es de Plotly. Para conocerla mejor, miren
    # https://dash.plot.ly/dash-core-components
    # y https://plot.ly/python/
    # y https://dash.plot.ly/dash-core-components/graph
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
    ###
])

# Si le ponen True aquí, tendrán Hot reloading
if __name__ == '__main__':
    app.run_server(debug=True)