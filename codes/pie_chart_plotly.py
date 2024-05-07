## Pie (Donut) Chart ##

import plotly.express as px

# Data
label_list = ['Brazil', 'Germany', 'Italy', 'Argentina', 'Uruguay', 'France', 'England', 'Spain']
freq = [5, 4, 4, 3, 2, 2, 1, 1]

# Customize colors
colors = ['darkorchid', 'royalblue', 'lightsteelblue', 'silver', 'sandybrown', 'lightcoral', 'seagreen', 'salmon']

# Building chart
fig = px.pie(values=freq, names=label_list, title='Countries with the most FIFA World Cup titles',
             color_discrete_map=dict(zip(label_list, colors)),
             labels={'label': 'Country', 'value': 'Frequency'},
             hole=0.3)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
