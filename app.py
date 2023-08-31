import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Initialize the app
external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css',
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server
app.title = "Sikandar Khattak's Dashboard"

# Pie chart data
labels = ['Year round bundle', 'Sprint and cuts bundle', 'Just snow removal', 'Just spring cleanup', 'Just cuts']
values = [7.87, 30.93, 17.57, 40.42, 4.81]

# Bar chart data
revenue_data = {
    'Year': ['2019', '2020', '2021', '2022', '2023'],
    'Revenue': [13.82, 38.71, 150.92, 260.83, 31.15]
}
df_revenue = pd.DataFrame(revenue_data)

# Line chart data
average_spent_data = {
    'Year': ['2019', '2020', '2021', '2022', '2023'],
    'Average Spent': [260.69, 190.69, 445.18, 491.20, 175.01]
}
df_average_spent = pd.DataFrame(average_spent_data)

# Average Lifespan
avg_lifespan = 126.16

# Create Pie Chart
fig_pie = px.pie(
    names=labels,
    values=values,
    title='Service Distribution'
)

# Create Bar Chart
fig_bar = px.bar(
    df_revenue,
    x='Year',
    y='Revenue',
    title='Annual Revenue'
)

# Create Line Chart
fig_line = px.line(
    df_average_spent,
    x='Year',
    y='Average Spent',
    title='Average Spent Per Year Per Customer'
)

# Set up the layout
# Set up the layout
app.layout = html.Div(style={'display': 'flex'}, children=[
    
    # Left Column
    html.Div(style={'flex': '50%'}, children=[
        
        # Image instead of text title
        html.Img(src='https://i.ibb.co/k8pBQv6/logo.jpg', alt='logo', style={'width': '200px'}),
        
        dcc.Graph(id='pie_chart', figure=fig_pie),
        
        dcc.Graph(id='bar_chart', figure=fig_bar),
    ]),
    
    # Vertical Line (Divider)
    html.Div(style={'borderLeft': '6px solid black', 'height': '100%', 'margin': '0 20px'}),
    
    # Right Column
    html.Div(style={'flex': '50%'}, children=[
        
        # Average Customer Lifespan
        html.H2("Average Customer Lifespan"),
        html.Div([
            html.H2(f"{avg_lifespan} Years", style={'font-size': '48px', 'font-weight': 'bold'})
        ], style={'text-align': 'center'}),
        html.Div([
            html.P("The average customer lifespan indicates the average number of years a customer continues to be a customer.")
        ], style={'text-align': 'center'}),
        
        # Line Chart for Average Spent
        dcc.Graph(id='line_chart', figure=fig_line),
    ])
])

# Run the app
if __name__ == '__main__':
    application.run(debug=True, port=8050)
