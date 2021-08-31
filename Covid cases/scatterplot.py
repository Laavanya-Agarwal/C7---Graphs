import pandas
import plotly.express as px

dataRef = pandas.read_csv('data.csv')
dataSort = px.scatter(dataRef, x='date', y='cases', 
                               color='country', title='Number of Covid Cases in Various countries')
dataSort.show()