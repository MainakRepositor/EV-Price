"""This module helps to preprocess the data."""

# Import necessary modules.
import pandas as pd
import streamlit as st

# Load the dataset.
@st.cache()
def load_data():
    """This function perform preprocessing on dataset and return that"""
    # read the dataset.
    df = pd.read_csv("./EV.csv")
    

    # Create list of final columns.
    final_col =  ['AccelSec','TopSpeed_KmH','Range_Km','Efficiency_WhKm','FastCharge_KmH','PowerTrain','PlugType','BodyStyle','Seats','Price']

    # Return the processed dataset.
    return df[final_col]

