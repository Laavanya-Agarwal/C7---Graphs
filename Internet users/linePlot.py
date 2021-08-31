import pandas
import plotly.express as px

dataRef = pandas.read_csv('line_chart.csv')
dataSort = px.line(dataRef, x='Year', y='Per capita income', color='Country', title='Line Graph')
dataSort.show()