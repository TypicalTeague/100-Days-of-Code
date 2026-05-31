import streamlit as st
import random

st.title("🔐 Password Generator")
st.write("Need a secure password? Adjust the sliders below to generate one.")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Streamlit sliders replace the terminal inputs
nr_letters = st.number_input("How many letters would you like?", min_value=0, max_value=20, value=8)
nr_symbols = st.number_input("How many symbols would you like?", min_value=0, max_value=10, value=2)
nr_numbers = st.number_input("How many numbers would you like?", min_value=0, max_value=10, value=2)

# Wrap the generator in a button
if st.button("Generate Password"):
    password_list = []

    for l in range(nr_letters):
        password_list.append(random.choice(letters))
    for s in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for n in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password = ''

    for i in password_list:
        password += i
        
    st.success(f"**{password}**")