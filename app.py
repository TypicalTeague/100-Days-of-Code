import streamlit as st

st.set_page_config(page_title="Andre's 100 Days of Code", layout="centered")

# Sidebar navigation to switch between days
project = st.sidebar.selectbox("Select a Project", ["Day 1: Band Name Generator", "Day 2: Coming Soon"])

if project == "Day 1: Band Name Generator":
    st.title("Welcome to the Band Name Generator 🎸")
    
    city = st.text_input("What's the name of the city you grew up in?")
    pet = st.text_input("What's your pet's name?")
    
    if st.button("Generate Band Name"):
        if city and pet:
            st.success(f"Your band name could be **{city} {pet}**")
        else:
            st.warning("Please fill out both fields first!")

elif project == "Day 2: Coming Soon":
    st.title("Day 2 Project")
    st.write("Stay tuned! Code is cooking.")