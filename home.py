"""This module creates the home page."""

# Import necessary modules.
import streamlit as st

def app():
    st.title("EV Price Pridictor")
    st.image("./welcome.jpg")
    st.markdown( '''Find out how much your dream EV can cost depending on the parameters''')
