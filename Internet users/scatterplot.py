import pandas
import plotly.express as px

dataRef = pandas.read_csv('data.csv')
dataSort = px.scatter(dataRef, x='Population', y='Per capita', 
                               color='Country', title='Scatter Graph', size='Percentage', size_max=60)
dataSort.show()