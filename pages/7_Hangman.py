import streamlit as st
import random
import hangman_words
import hangman_art

st.title("Day 7: Hangman 💀")

# Initialize the game's "memory" (session state)
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(hangman_words.word_list)
    st.session_state.lives = 6
    st.session_state.previous_guesses = []
    st.session_state.game_over = False
    st.session_state.status_message = ""
    st.session_state.guess_input = "" # This tracks the text box now!

# Display the Hangman Logo
st.text(hangman_art.logo)

# Game Reset Button
if st.button("Restart Game"):
    st.session_state.chosen_word = random.choice(hangman_words.word_list)
    st.session_state.lives = 6
    st.session_state.previous_guesses = []
    st.session_state.game_over = False
    st.session_state.status_message = ""
    st.session_state.guess_input = ""
    st.rerun()

st.divider()

# --- THE CALLBACK FUNCTION ---
# This runs instantly the second you press Enter
def process_guess():
    # Grab the letter the user just typed
    guess = st.session_state.guess_input.lower()
    
    # Instantly clear the text box for the next turn
    st.session_state.guess_input = "" 

    # If the box was empty or the game is over, do nothing
    if not guess or st.session_state.game_over:
        return

    # Process the logic
    if guess in st.session_state.previous_guesses:
        st.session_state.status_message = f"You already guessed '{guess}'. Try again."
    else:
        st.session_state.previous_guesses.append(guess)
        
        # Incorrect guess
        if guess not in st.session_state.chosen_word:
            st.session_state.lives -= 1
            st.session_state.status_message = f"'{guess}' is not in the word. You lost a life."
        else:
            st.session_state.status_message = f"Nice! '{guess}' is in the word."
        
        # Check for loss
        if st.session_state.lives == 0:
            st.session_state.game_over = True
            
        # Check for win
        win = True
        for letter in st.session_state.chosen_word:
            if letter not in st.session_state.previous_guesses:
                win = False
        if win:
            st.session_state.game_over = True

# --- THE UI DISPLAY ---
# Only run this if the game is still active
if not st.session_state.game_over:
    
    # Display lives and the actual image!
    st.write(f"**Lives Left:** {st.session_state.lives}")
    st.image(f"images/hangman_{st.session_state.lives}.png")

    # Build the display word (e.g., _ a _ _ l e)
    display = ""
    for letter in st.session_state.chosen_word:
        if letter in st.session_state.previous_guesses:
            display += letter + " "
        else:
            display += "_ "
            
    st.header(f"Word to guess: {display}")

    # Display the instant feedback message
    if st.session_state.status_message:
        st.info(st.session_state.status_message)

    # THE FIX: Tie the text box to the callback function using 'on_change'
    st.text_input("Guess a letter:", max_chars=1, key="guess_input", on_change=process_guess)

else:
    # What to show when the game is over
    st.image(f"images/hangman_{st.session_state.lives}.png")
    if st.session_state.lives == 0:
        st.error(f"Game Over! The word was **{st.session_state.chosen_word}**.")
    else:
        st.success("You survived!")