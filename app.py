#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
import datetime as dt


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('sample_set_manipulated.csv')

color_pallete = ['#DD4404','#f9bf3e','#383481','#474646']
count_id = df['id'].value_counts()
sex = df['sex'].str.capitalize()

fig_1 = px.bar(df['race_ethnicity'].value_counts(sort=True),
               title='Ethnicity',
               labels={'race_ethnicity':'Ethnicity',
                       'value':'Number of Clients',
                       'index':'Categories'},
               color_discrete_sequence=color_pallete,
               template='simple_white',
               orientation='h')
fig_1.update_layout(showlegend=False,
                    xaxis_visible=True,
                    xaxis_showticklabels=True,
                    margin_l=350)

fig_2 = px.pie(df, names=sex,
               values=count_id,
               title='Gender',
               labels={'sex':'Gender','values':'Number of clients','label':'Gender'},
               color_discrete_sequence=color_pallete)
fig_2.update_traces(textposition='inside', textinfo='percent+label')
fig_2.update_layout(showlegend=False)

fig_3 = px.bar(df['age_group'].value_counts(sort=True).sort_index(),
                     title='Age Groups',
                     labels={'age_group':'Age Groups',
                             'index':'Age Groups',
                             'value':'Number of Clients'},
                     color_discrete_map={'race_ethnicity':'#f9bf3e'},
                     template='simple_white',
                     orientation='v')
fig_3.update_layout(showlegend=False,margin_l=120)

fig_4 = px.pie(df, names='language',
               values=count_id,
               title='Language',
               labels={'language':'Language','values':'Number of clients'},
               color_discrete_sequence=color_pallete)
fig_4.update_traces(textposition='inside', textinfo='percent+label')
fig_4.update_layout(showlegend=False)

fig_5 = px.pie(df, names='dv_ht',
               values=count_id,
               title='Domestic Violence vs Human Trafficking',
               labels={'dv_ht':'Service Category','DV':'Domestic Violence','HT':'Human Trafficking','values':'Number of clients'},
               color_discrete_sequence=color_pallete)
fig_5.update_traces(textposition='inside', textinfo='percent+label')
fig_5.update_layout(showlegend=False)

fig_6 = px.histogram(df, x='service_date', y=count_id, color='dv_ht',
                     title='Domestic Violence vs Human Trafficking Over Time',
                     labels={'service_date':'Date',
                             'y':'Clients',
                             'dv_ht':'Service Category',
                             'DV':'Domestic Violence',
                             'HT':'Human Trafficking',
                             'values':'Number of clients'},
                     color_discrete_sequence=color_pallete,
                     template='simple_white')

fig_7 = px.pie(df, names='services_provided',
               values=count_id,
               title='Services Provided',
               labels={'services_provided':'Services Provided','values':'Number of clients'},
               color_discrete_sequence=color_pallete)
fig_7.update_traces(textposition='inside', textinfo='percent')
fig_7.update_layout(legend=dict(
       orientation='h',
        yanchor='top',
        y=-0.1,
        xanchor='right',
        x=1))

fig_8 = px.histogram(df, x='service_date', y=count_id, color='services_provided',
                     title='Services Provided Over Time',
                     labels={'service_date':'Date',
                             'services_provided':'Services Provided',
                             'y':'Clients',
                             'dv_ht':'Service Category',
                             'DV':'Domestic Violence',
                             'HT':'Human Trafficking',
                             'values':'Number of clients'},
                     color_discrete_sequence=color_pallete,
                     template='simple_white')
fig_8.update_layout(legend=dict(
       orientation='h',
        yanchor='bottom',
        y=-0.4,
        xanchor='auto',
        x=1.0))

# remove time delta and use only today's date with real data
today = dt.date.today()-dt.timedelta(days=10)
today_str = dt.datetime.strftime(today,'%Y-%m-%d')
total_clients_today = df[df.service_date==today_str]['id'].nunique()
card_1 = dbc.Card(
    [dbc.CardBody([html.H4('Current Number of Clients',
                            className='card-title',
                            style={'color':'#383481'}),
                   html.P(total_clients_today,
                          style={'color':'#474646'})
                  ])],
    )

total_clients = df['id'].nunique()
card_2 = dbc.Card(
    [dbc.CardBody([html.H4('Total Number of Clients',
                            className='card-title',
                            style={'color':'#383481'}),
                   html.P(total_clients,
                          style={'color':'#474646'})
                  ])],
    )


donate_button = dbc.Card(
    [dbc.CardBody([html.H4('Donate Now!',
                            className='card-title'),
                   dbc.Button('Click here',
                              href='https://pages.donately.com/rubysplace/fundraiser/daniel-abud-help-ruby-s-place-and-increase-your-impact',
                              className='mt-auto',
                              color='secondary')
                      ])],
     style={'color':'#DD4404'}
    )



app.layout = html.Div(children=[
                    html.Div([
                        html.Div(children=html.Img(
                                     src=app.get_asset_url('primary_logo.gif'),
                                     style={'width': '100%',
                                            'height': '100%'}),
                                     style={'width': '30%',
                                            'height': '100%',
                                            'padding': '25px'}),
                        html.Div([
                            html.H1(children="Ruby's Place by the numbers",
                                    style={'textAlign':'center',
                                           'font':'Arial',
                                           'border':'thick double #32alce',
                                           'padding':'25px',
                                           'font-variant':'small-caps'}),
                            html.H3(children='This is fictional data to serve as a placeholder',
                                    style={'textAlign':'center',
                                           'font':'Arial',
                                           'color':'#383481'})
                            ],
#                                 className="eleven columns"
                        )
                    ], className="row",
                       style={'display':'flex',
                              'flex-direction':'row'}),

#                        style={'display':'flex',
#                               'flex-direction':'column'},

                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),

                    html.H2(children='Overall Numbers',
                            style={'textAlign':'center',
                                   'font':'bold arial',
                                   'color':'#474646',
                                   'font-weight':'bold'}),

                    html.Div([
                        html.Div([card_1],style={'padding': '80px',
                                                 'textAlign':'center',
                                                 'fontSize':25,
                                                 'color':'#474646'}
                                         , className='four columns'),
                        html.Div([card_2],style={'padding': '80px',
                                                 'textAlign':'center',
                                                 'fontSize':25,
                                                 'color':'#474646'}
                                         , className='four columns'),
                        html.Div([donate_button],style={'padding': '80px',
                                                 'textAlign':'center',
                                                 'fontSize':25}
                                         , className='four columns')
                    ], className='row'),

                    html.Br(),
                    html.Br(),

                    html.H2(children='Demographics',
                            style={'textAlign':'center',
                                   'font':'Arial',
                                   'color':'#474646'}),

                    html.Br(),
                    html.Br(),

                    html.Div([
                        html.Div([dcc.Graph(figure=fig_2)], className="six columns"),
                        html.Div([dcc.Graph(figure=fig_4)], className="six columns")
                    ], className='row'),

                    html.Br(),
                    html.Br(),

                    html.Div([
                        html.Div([dcc.Graph(figure=fig_1)], className="seven columns"),
                        html.Div([dcc.Graph(figure=fig_3)], className="five columns")
                    ], className='row'),


                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),

                    html.H2(children='Services',
                            style={'textAlign':'center',
                                   'font':'Arial',
                                   'color':'#474646'}),

                    html.Br(),
                    html.Br(),

                    html.Div([
                        html.Div([dcc.Graph(figure=fig_5)], className="six columns"),
                        html.Div([dcc.Graph(figure=fig_7)], className="six columns")
                    ], className='row'),

                    html.Br(),
                    html.Br(),

                    html.Div([
                        html.Div([dcc.Graph(figure=fig_6)])
                    ], className='row'),

                    html.Br(),
                    html.Br(),

                    html.Div([
                        html.Div([dcc.Graph(figure=fig_8)])
                    ], className='row')

    ])


if __name__ == '__main__':
    server = app.server

