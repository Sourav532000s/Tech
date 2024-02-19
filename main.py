import streamlit as st
num1=st.number_input("Enter the number 1:")
num2=st.number_input("Enter the number 2:")


if st.button("Add"):
    st.write(f"# The total is{num1 + num2}")
    st.balloons()