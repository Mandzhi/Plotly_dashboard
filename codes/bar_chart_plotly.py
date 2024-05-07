## Bar Chart ##

import plotly.graph_objects as go

labels = ['Estádio do Maracanã', 'Camp Nou', 'Estadio Azteca',
          'Wembley Stadium', 'Rose Bowl', 'Estadio Santiago Bernabéu',
          'Estadio Centenario', 'Lusail Stadium']
capacity = [200, 121, 115, 99, 94, 90, 90, 89]

fig = go.Figure()

# Horizontal bar chart
fig.add_trace(go.Bar(y=labels, x=capacity, orientation='h', marker_color='blue'))

# Layout settings
fig.update_layout(title='Top-8 stadiums on capacity (in thousands)',
                  yaxis=dict(title='Stadiums'),
                  xaxis=dict(title='Capacity'),
                  showlegend=False,
                  plot_bgcolor='white')

fig.show()
