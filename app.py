import streamlit as st

st.title("BizSwap Demo")
st.write("This is a demo app to test Streamlit setup.")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Welcome to BizSwap.")
