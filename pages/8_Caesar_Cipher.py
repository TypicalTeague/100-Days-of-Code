import streamlit as st

st.title("Day 8: Caesar Cipher 🕵️‍♂️")
st.write("Encrypt or decrypt your secret messages below.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text.lower():
        if letter not in alphabet:
            # Keeps numbers, spaces, and symbols untouched
            output_text += letter
        else:
            if encode_or_decode == 'decode':
                shifted_position = alphabet.index(letter) - shift_amount
            else:
                shifted_position = alphabet.index(letter) + shift_amount
            
            # The % handles shifts larger than 26 so it wraps around the alphabet
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
            
    return output_text

# --- UI CONTROLS ---
direction = st.radio("What do you want to do?", ('encode', 'decode'))
text = st.text_area("Type your message:")
shift = st.number_input("Type the shift number:", min_value=1, step=1, value=3)

if st.button("Execute"):
    if text:
        result = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        st.success(f"**Here is the {direction}d result:**")
        st.code(result, language=None)
    else:
        st.warning("You need to type a message first!")