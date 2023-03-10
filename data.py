"""This create view data page"""

# Import necessary module
import streamlit as st

def app(df):
    # Give title
    st.title("View Data")

    # Create expander to show dataset data.
    with st.expander("View Data"):
        st.table(df)
    
    # Create a section to show info about dataset.
    st.header("Columns Summary:")

    # Show the describtion of dataset.
    if st.checkbox("Show Summary"):
        st.table(df.describe())

    # Creat a row with three columns to show info about columns.
    col1, col2, col3 = st.columns(3)

    # Add checkbox to show the columns name
    with col1:
        if st.checkbox("Show columns name"):
            st.table(df.columns)

    # Add checkbox to show the columns datatype
    with col2:
        if st.checkbox("View columns datatype"):
            dtypes_df = df.dtypes.apply(lambda x: x.name)
            st.table(dtypes_df)

    # Add checkbox to show the columns data.
    with col3:
        if st.checkbox("View column data"):
            column_data = st.selectbox("Select column", tuple(df.columns))
            st.write(df[column_data])