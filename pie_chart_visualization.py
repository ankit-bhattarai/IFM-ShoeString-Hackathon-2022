from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
app = Dash(__name__)
#
df = pd.read_csv ('example_data.csv', sep =' ')
#
df2 = df.set_axis(['Time', 'Power', 'Robot'], axis=1, inplace=False)


#df3 = px.data.tips()

fig = px.pie(df2, values='Power', names='Robot')
fig.show()
#print(df3)

# app.layout = html.Div([
#     dcc.Graph(
#         figure=dict(
#             data=[
#                 dict(
#                     x=df2['Time'],
#                     y=df2['Power'].loc[df2['Robot']=='robot1'],#df.loc[df['column_name'] == some_value]
#                     name='Robot 1',
#                     marker=dict(
#                         color='rgb(55, 83, 109)'
#                     )
#                 ),
#     dict(
#                     x=df2['Time'],
#                     y=df2['Power'].loc[df2['Robot']=='robot2'],#df.loc[df['column_name'] == some_value]
#                     name='Robot 2',
#                     marker=dict(
#                         color='rgb(26, 118, 255)'
#                     )
#                 )
#             ],
#             layout=dict(
#                 title='Robot Power',
#                 showlegend=True,
#                 legend=dict(
#                     x=0,
#                     y=1.0
#                 ),
#                 margin=dict(l=40, r=0, t=40, b=30)
#             )
#         ),
#         style={'height': 300},
#         id='my-graph'
#     )
#
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

