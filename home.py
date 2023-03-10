"""This module creates the home page."""

# Import necessary modules.
import streamlit as st

def app():
    st.title("Car Pridiction app")
    st.image("./welcome.jpg")
    st.text(
        """
        Find out how much your dream EV can cost depending on the parameters
         """
    )