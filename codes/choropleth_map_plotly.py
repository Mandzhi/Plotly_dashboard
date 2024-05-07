## Choropleth Map ##

import polars as pl
import plotly.express as px

df = pl.read_csv('data_football.csv')
df.head(5)
fig = px.choropleth(df, locations='team_code', color='count', 
                    hover_name='team_name', projection='natural earth',
                    title='Geography of the FIFA World Cups',
                    color_continuous_scale='Reds')
fig.show()
