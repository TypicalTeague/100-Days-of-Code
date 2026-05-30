import streamlit as st
st.title("Welcome to the Band Name Generator 🎸")
    
city = st.text_input("What's the name of the city you grew up in?")
pet = st.text_input("What's your pet's name?")

if st.button("Generate Band Name"):
    if city and pet:
        st.success(f"Your band name could be **{city} {pet}**")
    else:
        st.warning("Please fill out both fields first!")
