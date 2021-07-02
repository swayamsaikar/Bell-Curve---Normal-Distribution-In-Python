# Importing all the modules
import plotly.figure_factory as ff
import plotly.express as px
import pandas


def CurveDistri(column_name):
    # reading the csv and storing all the data in df variable
    df = pandas.read_csv('data.csv')

    # getting all the avg data of the dataFrame and storing all the avgs as a list in avg variable
    data = list(df[column_name])

    # Creating a distplot graph to show the Normal distribution of the avg data
    figure = ff.create_distplot([data], ["name"], show_hist=False)

    # Showing the figure
    figure.show()


def MyBar():
    # reading the csv and storing all the data in df variable
    df = pandas.read_csv('data.csv')

    # Creating a Bar Graph
    figure = px.bar(df, x="Mobile Brand", y="Avg Rating")
    figure.show()


columnInput = input(
    "Enter The Name of the Column for which you want to find the Bell Curve Distribution").lower()

if "avg rating" in columnInput:
    CurveDistri("Avg Rating")
elif "mobile brand" in columnInput:
    MyBar()
else:
    print(f"No column available with the name {columnInput} ")
