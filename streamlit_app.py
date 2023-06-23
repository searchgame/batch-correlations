import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

"""
# Batch correlations 

Quickly uncover potential relationships in your data by getting an overview of correlation coefficients between multiple pairs of metrics.

See the code and how to interpret the charts [on the Github repo](https://github.com/searchgame/ga-correlations/).

Made by [Victor Gras](https://victorgras.com)
"""

# Set a title
st.title('Results:')

# Set a sidebar for user input
st.sidebar.title("Settings")

# Upload the CSV file
file_upload = st.sidebar.file_uploader("Upload CSV", type=['csv'])

# Check if a file is uploaded
if file_upload is not None:
    # Load the CSV file
    data = pd.read_csv(file_upload, header=None)

    # Set the first row as column names
    data.columns = data.iloc[0].values
    data = data.iloc[1:]

    # Remove first column
    data = data.iloc[:, 1:]

    # Convert data to numeric
    data = data.apply(pd.to_numeric, errors='coerce')

    # Compute correlation matrix
    corr = data.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with the mask
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    plt.title('Correlation of your data')

    # Show the plot in Streamlit
    st.pyplot(fig)

else:
    st.sidebar.text('Please upload a CSV file.')
