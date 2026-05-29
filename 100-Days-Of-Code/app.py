import streamlit as st

st.set_page_config(page_title="Andre's 100 Days of Code", layout="centered")

# Sidebar navigation to switch between days
project = st.sidebar.selectbox("Select a Project", ["Day 1: Band Name Generator", "Day 2: Tip Calculator", "Day 3: Treasure Island"])

if project == "Day 1: Band Name Generator":
    st.title("Welcome to the Band Name Generator 🎸")
    
    city = st.text_input("What's the name of the city you grew up in?")
    pet = st.text_input("What's your pet's name?")
    
    if st.button("Generate Band Name"):
        if city and pet:
            st.success(f"Your band name could be **{city} {pet}**")
        else:
            st.warning("Please fill out both fields first!")

elif project == "Day 2: Tip Calculator":
    st.title("Welcome to the Tip Calculator 💸")
    st.write("Calculate the split for your bill quickly.")
    
    # Using number inputs instead of terminal inputs
    total_bill = st.number_input("What was the total bill? ($)", min_value=0.0, step=0.01, format="%.2f")
    
    # A slider selection works beautifully for choosing percentages
    tip_percentage = st.slider("How much tip would you like to give? (%)", min_value=0, max_value=100, value=12)
    
    split_people = st.number_input("How many people to split the bill with?", min_value=1, value=1, step=1)
    
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
elif project == "Day 3: Treasure Island":
    st.title("🏴‍☠️ Treasure Island")
    
    
    st.code('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''')
    
    st.subheader("Welcome to Treasure Island.")
    st.write("Your mission is to find the treasure.")
    st.divider()

    # Remember user choices
    if "step" not in st.session_state:
        st.session_state.step = 1

    # Restart button
    if st.sidebar.button("Restart Adventure"):
        st.session_state.step = 1
        st.rerun()

    # --- Choice 1 ---
    if st.session_state.step == 1:
        st.write("You've arrived at a crossroads. You have 2 choices.")
        col1, col2 = st.columns(2)
        if col1.button("Go Left 👈"):
            st.session_state.step = 2
            st.rerun()
        if col2.button("Go Right 👉"):
            st.session_state.step = "lost_forever"
            st.rerun()

    # --- Choice 2 ---
    elif st.session_state.step == 2:
        st.write("After walking for what seems like an hour, you arrive at a lake. In the middle of the lake you notice a small house sitting on a tiny piece of land.")
        col1, col2 = st.columns(2)
        if col1.button("Swim Across 🏊‍♂️"):
            st.session_state.step = "trout_attack"
            st.rerun()
        if col2.button("Wait ⏳"):
            st.session_state.step = 3
            st.rerun()

    # --- Choice 3 ---
    elif st.session_state.step == 3:
        st.write("Your patience has been rewarded. You notice that the water is not nearly as calm as you once thought. It's teeming with life, and they don't seem too keen on having visitors. Looking a little ways down to your right, you notice a boat. It's not in the best shape, but it's sturdy enough.")
        st.write("The ride over was not smooth at all, but you've made it across nonetheless. Walking closer to the house you notice 3 distinct doors in the front. They're all identical in every way, but color.")
        
        col1, col2, col3 = st.columns(3)
        if col1.button("🔴 Red Door"):
            st.session_state.step = "fire_death"
            st.rerun()
        if col2.button("🟡 Yellow Door"):
            st.session_state.step = "win"
            st.rerun()
        if col3.button("🔵 Blue Door"):
            st.session_state.step = "mimic_death"
            st.rerun()

    # --- End States ---
    elif st.session_state.step == "lost_forever":
        st.error("You walk down the path for what seems like hours with no end in sight. Eventually you give up and turn around to walk back, but realize there's nothing behind you. The path has now disappeared and it's only trees. You're now lost forever.\n\nGame Over.")
        
    elif st.session_state.step == "trout_attack":
        st.error("The water was not as peaceful as it seemed. You were attacked by trout halfway to the house.\n\nGame Over.")
        
    elif st.session_state.step == "fire_death":
        st.error("As soon as you touch the door you are engulfed in flames and collapse into a pile of ash on the ground.\n\nGame Over.")
        
    elif st.session_state.step == "mimic_death":
        st.error("Before you can even touch the door, you see it split into two and reveals a massive jaw with sharp teeth. It clamps down on your body and swallows you in one gulp.\n\nGame Over.")
        
    elif st.session_state.step == "win":
        st.success("Opening the door, you are blinded by more gold than you've ever seen in your life. Judging by the rocky ride over, you understand this will be weeks of carrying it all back to the island. Time well spent based on how rich you'll become.\n\nYou Win!! 🎉")