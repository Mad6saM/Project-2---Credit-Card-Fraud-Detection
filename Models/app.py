import streamlit as st
import pickle

st.title("Credit Card Fraud Detection")

Input = st.text_input("Enter 0 for Fair, 1 for Fraud", "")

if Input.isdigit() and Input in ['0', '1']:
    Input = int(Input)

    if st.button("Submit"):
        if Input == 0:
            result = "Fair"
        else:
            result = "Fraud"

        st.write("Result:", result)

else:
    st.warning("Please enter a valid digit (0 or 1).")
