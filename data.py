"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st


def app(df):
    """This function create the Data Info page"""

    # Add title to the page
    st.title("Data Info page")

    # Add subheader for the section
    st.subheader("View Data")

    # Create an expansion option to check the data
    st.dataframe(df)

   
