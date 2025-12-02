import streamlit as st
import pandas as pd
import plotly.express as px

def get_data(x_axis, y_axis):
    df = pd.read_csv("happy.csv")
    x_data = df[x_axis]
    y_data = df[y_axis]
    return x_data, y_data


st.title("In Search for Happiness")

options = ("GDP", "Happiness", "Generosity", "Corruption")

x = st.selectbox("Select the data for the x-axis", options)

y = st.selectbox("Select the data for the y-axis", options)

x_axis, y_axis = get_data(x.lower(), y.lower())

st.subheader(f"{x} and {y}")

figure = px.scatter(x=x_axis,
                 y=y_axis,
                 labels={"x": x, "y": y})

st.plotly_chart(figure)