# In Search for Happiness
This is a simple Streamlit app that lets you explore relationships between different happiness-related factors. The app loads data from happy.csv and displays an interactive scatter plot based on the variables you choose.

## How It Works

1. Choose two factors (GDP, Happiness, Generosity, or Corruption).

2. The app loads the corresponding columns from the dataset.

3. A scatter plot is generated using Plotly to show how the two factors relate.

## Features

- Interactive dropdown menus

- Automatic data loading from happy.csv

- Plotly scatter plot visualization

- Clean and simple user interface

## Requirements

- Python 3.x

- Streamlit

- Pandas

- Plotly

### Install them with
```
pip install streamlit pandas plotly
```
### Running the App
```
streamlit run app.py
```
Make sure that happy.csv is in the same directory as your Python script
