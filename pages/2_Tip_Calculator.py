import streamlit as st
st.title("Welcome to the Tip Calculator 💸")
st.write("Calculate the split for your bill quickly.")

# Using number inputs instead of terminal inputs
total_bill = st.number_input("What was the total bill? ($)", min_value=0.0, format="%.2f")

# A slider selection works beautifully for choosing percentages
tip_percentage = st.number_input("How much tip would you like to give? (%)", min_value=0, max_value=100)

split_people = st.number_input("How many people to split the bill with?", min_value=1, value=1)

if st.button("Calculate Split"):
    if total_bill > 0:
        # Math logic converted from standard Python math
        tip_amount = total_bill * (tip_percentage / 100)
        grand_total = total_bill + tip_amount
        per_person_pay = grand_total / split_people
        
        # Displays the final amount rounded 
        st.success(f"Each person should pay: **${per_person_pay:.2f}**")
    else:
        st.warning("Please enter a valid bill total.")