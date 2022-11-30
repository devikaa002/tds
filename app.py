import streamlit as st

st.title("Multiplication of two numbers")
a=st.number_input("Enter 1st number")
b=st.number_input("Enter 2nd number")
c=a*b
st.write(c)
