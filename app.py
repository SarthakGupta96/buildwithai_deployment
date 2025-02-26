from joblib import load
from numpy import array

import streamlit as st

model = load("model.pkl")

st.title("Placement Package Calculator")
st.write("Enter CGPA")


cgpa_input = st.number_input("CGPA",
                             max_value=10.0,
                             min_value=0.0,
                             step=0.1)



if st.button("Predict"): 
    inputf = array([[cgpa_input]])
    prediction = model.predict(inputf)[0]
    st.success(f"Predicted Package: {prediction:.2f}")
