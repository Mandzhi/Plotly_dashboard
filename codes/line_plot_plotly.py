## Line Plot ##

import plotly.graph_objects as go

time = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
numbers = [48411, 68626, 44676, 42571, 52609, 49499, 53772, 47371]
labels = ['Italy', 'USA', 'France', 'Japan / South Korea', 'Germany', 
'South Africa', 'Brazil', 'Russia']

fig = go.Figure()

# Line plot
fig.add_trace(go.Scatter(x=time, y=numbers, mode='lines+markers',
                         marker=dict(color='black',size=10), line=dict(width=2.5)))

# Scatter plot
for i in range(len(time)):
    fig.add_trace(go.Scatter(x=[time[i]], y=[numbers[i]],
                             mode='markers', name=labels[i]))

# Layout settings
fig.update_layout(title='Average number of attendees per game in 1990-2018',
                  xaxis=dict(tickvals=time),
                  yaxis=dict(range=[35000, 70000]),
                  showlegend=True,
                  legend=dict(x=0.5, y=-0.2),
                  plot_bgcolor='white')

fig.show()
