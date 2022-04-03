import json
import pathlib
import pandas as pd

from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import plotly.express as px

external_stylesheets = [dbc.themes.DARKLY]
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets/").resolve()
print(DATA_PATH)



#california_geojson_address=DATA_PATH.joinpath("/geojson/zip/individual_states/ca_california_zip_codes_geo.min.json")
california_geojson_address="../datasets/geojson/zip/individual_states/ca_california_zip_codes_geo.min.json"
temp_file=open(california_geojson_address,'r')
california_geo=json.load(temp_file)
temp_file.close()
for feature in california_geo['features']:
    feature['id'] = feature['properties']['ZCTA5CE10']

zillow_dataset_address="../datasets/zillow_dataset/home_value_index/zip/Zip_zhvi_uc_sfr_tier_0.33_0.67_sm_sa_month.csv"
zillow_dataset=pd.read_csv(zillow_dataset_address)



app.layout=html.Div(
    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        html.H2("TEXT", className='text-center'),
                        html.Br(),
                        dbc.Card(
                            children=[
                                dbc.CardBody(
                                    html.H4(
                                        "TEXT", className='text-center')
                                )
                            ]
                        )
                    ],
                    width={'size':4}#,
                    #align='center'
                )
            ],
            justify='center'
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Card(
                            children=[
                                dbc.CardBody(
                                    dcc.Dropdown(
                                            id='FIX2',
                                            # options=[
                                                
                                            #     ],
                                            multi=False,
                                            style={
                                                'color': '#212121',
                                                'background-color': '#3EB489',
                                            }
                                        )
                                )
                            ]
                        )
                    ]
                ),
                dbc.Col(
                    children=[
                        dbc.Card(
                            children=[
                                dbc.CardBody(
                                    dcc.Dropdown(
                                            id='FIX3',
                                            # options=[
                                                
                                            #     ],
                                            multi=False,
                                            style={
                                                'color': '#212121',
                                                'background-color': '#3EB489',
                                            }
                                        )
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        html.H2("TEXT", className='text-center'),
                        html.Br(),
                        dbc.Card(
                            children=[
                                dbc.CardBody(
                                    dbc.Card(
                                        dcc.Graph(
                                            id='basic_choropleth',
                                            figure=px.choropleth_mapbox(
                                                zillow_dataset,
                                                geojson=california_geo,
                                                locations='RegionName',
                                                labels={'current_date':'2022-02-28'},
                                                mapbox_style="carto-positron",
                                                center={"lat": 38.5816, "lon": -100.4944},
                                                color='2022-02-28',
                                                opacity=0.5,
                                                range_color=(4e5,1.5e6)
                                            )
                                        )
                                    ),
                                )
                            ]
                        )
                    ],
                    width={'size':12}#,
                    #align='center'
                )
            ],
            justify='center'
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)