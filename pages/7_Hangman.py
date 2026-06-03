import streamlit as st
import random
import hangman_words

st.title("Day 7: Hangman 💀")

# Initialize the game's "memory" (session state)
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(hangman_words.word_list)
    st.session_state.lives = 6
    st.session_state.previous_guesses = []
    st.session_state.game_over = False
    st.session_state.status_message = ""
    st.session_state.guess_input = "" 

# Display the Hangman Logo
st.image("images/hangman_logo.png")

# Game Reset Button

st.divider()

# THE CALLBACK FUNCTION
def process_guess():
    guess = st.session_state.guess_input.lower()
    st.session_state.guess_input = "" 

    if not guess or st.session_state.game_over:
        return

    if guess in st.session_state.previous_guesses:
        st.session_state.status_message = f"You already guessed '{guess}'. Try again."
    else:
        st.session_state.previous_guesses.append(guess)
        
        if guess not in st.session_state.chosen_word:
            st.session_state.lives -= 1
            st.session_state.status_message = f"'{guess}' is not in the word. You lost a life."
        else:
            st.session_state.status_message = f"Nice! '{guess}' is in the word."
        
        if st.session_state.lives == 0:
            st.session_state.game_over = True
            
        win = True
        for letter in st.session_state.chosen_word:
            if letter not in st.session_state.previous_guesses:
                win = False
        if win:
            st.session_state.game_over = True

# THE UI DISPLAY
if not st.session_state.game_over:
    
    st.write(f"**Lives Left:** {st.session_state.lives}")
    
    # Back to ASCII art
    st.image(f"images/hangman_{st.session_state.lives}.png")

    display = ""
    for letter in st.session_state.chosen_word:
        if letter in st.session_state.previous_guesses:
            display += letter + " "
        else:
            display += "_ "
            
    st.header(f"Word to guess: {display}")

    if st.session_state.status_message:
        st.info(st.session_state.status_message)

    st.text_input("Guess a letter:", max_chars=1, key="guess_input", on_change=process_guess)

else:
    # Back to ASCII art for the game over screen
    st.image(f"images/hangman_{st.session_state.lives}.png")
    if st.session_state.lives == 0:
        st.error(f"Game Over! The word was **{st.session_state.chosen_word}**.")
    else:
        st.success("You survived!")

# --- VISUAL KEYBOARD ---
keyboard_html = "<div style='display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-top: 20px;'>"
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter in st.session_state.previous_guesses:
        if letter in st.session_state.chosen_word:
            # Right guess gets green
            style = "background-color: #28a745; color: white; border: 1px solid #28a745;"
        else:
            # Wrong guess gets dark grey
            style = "background-color: #6c757d; color: white; border: 1px solid #6c757d;"
    else:
        # Unused letters stay hollow
        style = "background-color: transparent; border: 1px solid #888; color: inherit;"
        
    keyboard_html += f"<div style='padding: 10px 15px; border-radius: 5px; font-weight: bold; text-transform: uppercase; {style}'>{letter}</div>"
keyboard_html += "</div>"

# Render the HTML block at the bottom of the page
st.markdown(keyboard_html, unsafe_allow_html=True)

if st.button("Restart Game"):
    st.session_state.chosen_word = random.choice(hangman_words.word_list)
    st.session_state.lives = 6
    st.session_state.previous_guesses = []
    st.session_state.game_over = False
    st.session_state.status_message = ""
    st.session_state.guess_input = ""
    st.rerun()