import dash
import dash_core_components as dcc
import dash_html_components as html

# PODEMOS IMPORTAR LO QUE QUERAMOS!
import pandas as pd

# podemos importar PLOTLY
import plotly.graph_objs as go

exports = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

life_expectancy = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# children es un array, nada más. Lo que hay que hacer es poner los elementos en 
# orden y listo

# todo va dentro de un Div. Qué es un div?
app.layout = html.Div(children=[
    
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(exports),
    generate_table(life_expectancy),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=life_expectancy[life_expectancy['continent'] == i]['gdp per capita'],
                    y=life_expectancy[life_expectancy['continent'] == i]['life expectancy'],
                    text=life_expectancy[life_expectancy['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in life_expectancy.continent.unique()
            ],
            # el layout es super configurable, aquí es donde se crea el idiom de TM
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    # es bueno dejar siempre la coma aqu
])




if __name__ == '__main__':
    app.run_server(debug=True)