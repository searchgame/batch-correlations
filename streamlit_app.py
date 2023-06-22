import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
# Google Analytics correlations 

Quickly get an overview of correlations between pairs of Google Analytics metrics.
"""

# Set a title
st.title('Google Analytics Correlation App')

# Set a sidebar for user input
st.sidebar.title("Settings")

# Upload the CSV file
file_upload = st.sidebar.file_uploader("Upload CSV", type=['csv'])

# Check if a file is uploaded
if file_upload is not None:
    # Load the CSV file
    data = pd.read_csv(file_upload, header=None)
    
    # Remove rows till "Results Breakdown" appears
    while data.iloc[0,0] != "Results Breakdown":
        data = data.iloc[1:]
    data = data.iloc[1:]

    # Set the first row as column names
    data.columns = data.iloc[0].values
    data = data.iloc[1:]

    # Remove first column
    data = data.iloc[:, 1:]

    # Remove 'ga:' from the column names
    data.columns = data.columns.str.replace('ga:', '')

    # Convert data to numeric
    data = data.apply(pd.to_numeric, errors='coerce')

    # Plotting correlation heatmap and saving as a PDF file
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    plt.title('Correlation of your data')

    # Show the plot in Streamlit
    st.pyplot(fig)

else:
    st.sidebar.text('Please upload a CSV file.')
