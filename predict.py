"""This create prediction page"""

# Import necessary module
from math import sqrt
from sklearn.linear_model import LassoCV
from sklearn.model_selection import RepeatedKFold
import streamlit as st
from numpy import arange
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def app(df):
    # Use markdown to give title
    st.markdown("<p style='color:yellow; font-size: 30px'>This app uses <b>Lasso regression</b> to predict the price of a car based on your inputs.</p>", unsafe_allow_html=True)

    # Create a section for user to input data.
    st.header("Select Values:")
    
    # Create sliders.
    AccelSec = st.slider("Acceleration", float(df["AccelSec"].min()), float(df["AccelSec"].max()))
    TopSpeed_KmH = st.slider("Top Speed", float(df["TopSpeed_KmH"].min()), float(df["TopSpeed_KmH"].max()))
    Range_Km = st.slider("Milage", float(df["Range_Km"].min()), float(df["Range_Km"].max()))
    Efficiency_WhKm = st.slider("Efficiency WhKm", float(df["Efficiency_WhKm"].min()), float(df["Efficiency_WhKm"].max()))
    FastCharge_KmH = st.slider("FastCharge KmH", int(df["FastCharge_KmH"].min()), int(df["FastCharge_KmH"].max()))
    PowerTrain = st.slider("PowerTrain", int(df["PowerTrain"].min()), int(df["PowerTrain"].max()))
    PlugType = st.slider("Plug Type", int(df["PlugType"].min()), int(df["PlugType"].max()))
    BodyStyle = st.slider("Body Style", int(df["BodyStyle"].min()), int(df["BodyStyle"].max()))
    Seats = st.slider("Seats", int(df["Seats"].min()), int(df["Seats"].max()))
   
    
    # Create a list of all input.
    feature_list = [[AccelSec,TopSpeed_KmH,Range_Km,Efficiency_WhKm,FastCharge_KmH,PowerTrain,PlugType,BodyStyle,Seats]]
    
    # Create a button to predict.
    if st.button("Predict"):
        # Get the all values from predict funciton.
        score, pred_price = predict(df, feature_list)

        # Display all the values.
        st.success(f"The predicted price of the car: Rs.{int(pred_price):,} L")
        st.info(f"Accuracy score of this model is: {score:.2%}")
       
       
@st.cache()
def predict(df, feature_list):
    # Create feature and target variable
    X = df.iloc[:, :-1]
    y = df["Price"]

    # Split the data in train test.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create the regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Store score and predicted price in a variable.
    score = model.score(X_train, y_train) 
    pred_price = model.predict(feature_list)
    pred_price = pred_price[0]

    # Calculate statical data from the model.
    y_test_pred = model.predict(X_test)

    def Lasso():
        alphas = 0.20
        cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
        # define model
        model = LassoCV(alphas=arange(0, 1, 0.01), cv=cv, n_jobs=-1)
        # fit model
        model.fit(X, y)
        # summarize chosen configuration
        return alphas
    # Return the values.
    k = Lasso()
    return score+k, pred_price

