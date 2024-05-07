import polars as pl
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

header = html.H2(children="FIFA World Cup Analysis")

## Line plot with scatters ##

# Data
time = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
numbers = [48411, 68626, 44676, 42571, 52609, 49499, 53772, 47371]
labels = ['Italy', 'USA', 'France', 'Japan / South Korea', 'Germany', 'South Africa', 'Brazil', 'Russia']

# Building chart
chart1 = go.Figure()

chart1.add_trace(go.Scatter(x=time, y=numbers, mode='lines+markers',
                         marker=dict(color='black',size=10), line=dict(width=2.5)))

for i in range(len(time)):
    chart1.add_trace(go.Scatter(x=[time[i]], y=[numbers[i]],
                             mode='markers', name=labels[i]))

# Layout settings
chart1.update_layout(title='Average number of attendees per game in 1990-2018',
                  xaxis=dict(tickvals=time),
                  yaxis=dict(range=[35000, 70000]),
                  showlegend=True,
                  plot_bgcolor='white')


plot1 = dcc.Graph(
        id='plot1',
        figure=chart1,
        className="six columns"
    )

## Pie chart ##

# Data
label_list = ['Brazil', 'Germany', 'Italy', 'Argentina', 'Uruguay', 'France', 'England', 'Spain']
freq = [5, 4, 4, 3, 2, 2, 1, 1]

# Customize colors
colors = ['darkorchid', 'royalblue', 'lightsteelblue', 'silver', 'sandybrown', 'lightcoral', 'seagreen', 'salmon']

# Building chart
chart2 = px.pie(values=freq, names=label_list, title='Countries with the most FIFA World Cup titles',
             color_discrete_map=dict(zip(label_list, colors)),
             labels={'label': 'Country', 'value': 'Frequency'},
             hole=0.3)

chart2.update_traces(textposition='inside', textinfo='percent+label')

plot2 = dcc.Graph(
        id='plot2',
        figure=chart2,
        className="six columns"
    )

## Horizontal bar chart ##

labels = ['Estádio do Maracanã', 'Camp Nou', 'Estadio Azteca',
          'Wembley Stadium', 'Rose Bowl', 'Estadio Santiago Bernabéu',
          'Estadio Centenario', 'Lusail Stadium']
capacity = [200, 121, 115, 99, 94, 90, 90, 89]

# Building chart
chart3 = go.Figure()

chart3.add_trace(go.Bar(y=labels, x=capacity, orientation='h', marker_color='blue'))

# Layout settings
chart3.update_layout(title='Top-8 stadiums on capacity (in thousands)',
                  yaxis=dict(title='Stadiums'),
                  xaxis=dict(title='Capacity'),
                  showlegend=False,
                  plot_bgcolor='white')

 
plot3 = dcc.Graph(
        id='plot3',
        figure=chart3,
        className="six columns"
    )

## Chropleth map ##

# Data
df = pl.read_csv('data_football.csv')

# Building chart
chart4 = px.choropleth(df, locations='team_code', color='count', 
                    hover_name='team_name', projection='natural earth',
                    title='Geography of the FIFA World Cups',
                    color_continuous_scale='Reds')

plot4 = dcc.Graph(
        id='plot4',
        figure=chart4,
        className="six columns"
    )


row1 = html.Div(children=[plot1, plot2],)
row2 = html.Div(children=[plot3, plot4])
layout = html.Div(children=[header, row1, row2], style={"text-align": "center"})

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=False)
