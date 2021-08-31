import pandas
import plotly.express as px

dataRef = pandas.read_csv('data.csv')
dataSort = px.bar(dataRef, x='Country', y='InternetUsers', color='Country', title='Bar Graph')
dataSort.show()