import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # dense cuenta que tenemos id para identificarlo en el callback y un value inicial, importante!
    # el value inicial debe ser algo que tenga sentido, pues es lo que se renderiza (1 vez o la 1era vez)
    dcc.Input(id='my-id', value='initial value', type='text'),
    # usamos id's en los componentes de HTML para cambiarlos desde los callbacks
    html.Div(id='my-div')

])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

# la(s) variable(s) que entran como parámetro deben venir en orden y ser súper claras
# los callbacks están asociados a acciones, así que pongan un nombre asociado a una acción
# deben retornar el valor correcto

if __name__ == '__main__':
    app.run_server(debug=True)