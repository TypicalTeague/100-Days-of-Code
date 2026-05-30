import streamlit as st
st.title("Rock Paper Scissors")
st.write("Select your move to play against the CPU.")

# Initialize ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
'''

hand_sign = [rock, paper, scissors]

# Create layout columns for the selection buttons
col1, col2, col3 = st.columns(3)
user_choice = None

if col1.button("Rock"):
    user_choice = 0
if col2.button("Paper"):
    user_choice = 1
if col3.button("Scissors"):
    user_choice = 2

# Run game logic if a button was pressed
if user_choice is not None:
    import random
    cpu_choice = random.randint(0, 2)
    
    # Display the selections side by side
    display_col1, display_col2 = st.columns(2)
    
    with display_col1:
        st.subheader("You Chose:")
        st.code(hand_sign[user_choice])
        
    with display_col2:
        st.subheader("CPU Chose:")
        st.code(hand_sign[cpu_choice])
        
    st.divider()

    # Determine the winner using your logic
    if user_choice == cpu_choice:
        st.info("It's a tie!")
    elif user_choice == 0 and cpu_choice == 2:
        st.success("You Win!")
    elif user_choice == 2 and cpu_choice == 0:
        st.error("You Lose.")
    elif user_choice > cpu_choice:
        st.success("You Win!")
    else:
        st.error("You Lose.")