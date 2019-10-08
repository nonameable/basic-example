import dash
import dash_core_components as dcc
import dash_html_components as html

# PODEMOS IMPORTAR LO QUE QUERAMOS!
import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

colors = {
    'background': '#111111',
    'text': '#1c506a'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# children es un array, nada más. Lo que hay que hacer es poner los elementos en 
# orden y listo
app.layout = html.Div(children=[
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
    ),
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df),

])




if __name__ == '__main__':
    app.run_server(debug=True)