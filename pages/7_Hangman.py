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

# Display the Hangman Logo
st.text(hangman_art.logo)

# Game Reset Button
if st.button("Restart Game"):
    st.session_state.chosen_word = random.choice(hangman_words.word_list)
    st.session_state.lives = 6
    st.session_state.previous_guesses = []
    st.session_state.game_over = False
    st.rerun()

st.divider()

# Only run this logic if the game is still active
if not st.session_state.game_over:
    
    # Display lives and art
    st.write(f"**Lives Left:** {st.session_state.lives}")
    st.text(hangman_art.stages[st.session_state.lives])

    # Build the display word (e.g., _ a _ _ l e)
    display = ""
    for letter in st.session_state.chosen_word:
        if letter in st.session_state.previous_guesses:
            display += letter + " "
        else:
            display += "_ "
            
    st.header(f"Word to guess: {display}")

    # Player Input
    guess = st.text_input("Guess a letter:", max_chars=1).lower()

    if guess:
        if guess in st.session_state.previous_guesses:
            st.info(f"You already guessed '{guess}'. Try again.")
        else:
            st.session_state.previous_guesses.append(guess)
            
            # Incorrect guess
            if guess not in st.session_state.chosen_word:
                st.session_state.lives -= 1
                st.warning(f"You guessed '{guess}', that's not in the word. You lose a life.")
            
            # Check for loss
            if st.session_state.lives == 0:
                st.session_state.game_over = True
                st.error("*********************** YOU LOSE ***********************")
                st.write(f"The word was: **{st.session_state.chosen_word}**")
                st.rerun()
                
            # Check for win
            win = True
            for letter in st.session_state.chosen_word:
                if letter not in st.session_state.previous_guesses:
                    win = False
                    
            if win:
                st.session_state.game_over = True
                st.success("**************************** YOU WIN ****************************")
                st.rerun()
                
        # Force a refresh to update the display immediately after a guess
        if not st.session_state.game_over:
            st.rerun()

else:
    # What to show when the game is over
    st.text(hangman_art.stages[st.session_state.lives])
    if st.session_state.lives == 0:
        st.error(f"Game Over! The word was **{st.session_state.chosen_word}**.")
    else:
        st.success("You survived!")