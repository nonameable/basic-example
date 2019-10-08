# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# aquí pueden crear todas las variables que necesiten. 
# Tengan en cuenta que entre más cosas hagan aquí, más se demora la carga inicial
# de la app
# https://www.color-hex.com/
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Miren cómo mandamos el paramétro de estilo. Esto es equivalente a hacer
# https://www.w3schools.com/html/tryit.asp?filename=tryhtml_css_inline
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    # miren como omitimos children. Como es el primer parámetro, podemos hacerlo.
    html.H1(
        'Hola Dash desde Scipy Latam',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    # aquí hacemos lo mismo
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)