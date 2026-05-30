import streamlit as st
import streamlit as st

# Configure the main page settings
st.set_page_config(
    page_title="Andre's 100 Days of Code",
    page_icon="✌️",
    layout="centered"
)

# Main Header
st.title("Just some code. ✌️")

# Personal Introduction
st.subheader("Hey, I'm Andre.")
st.write("""
I'm wrapping up my CS degree at Georgia State. Mostly, I just like messing around with Python, data, and seeing how machine learning can make things run a bit smoother.
""")

st.divider()

# Project Description
st.write("""
### What's all this?
Honestly, I'm just doing the **100 Days of Code** challenge to stay sharp and have somewhere to dump my projects. 

If you look at the sidebar, you'll see whatever apps, games, and scripts I've put together lately. Nothing too crazy, just figuring things out and building stuff as I go.
""")

col1, col2 = st.columns(2)

with col1:
    # Make sure these paths match your exact file names!
    st.page_link("pages/band_name_generator.py", label="Day 1: Band Name Generator", icon="🎸")
    st.page_link("pages/treasure_island.py", label="Day 3: Treasure Island", icon="🏴‍☠️")

with col2:
    st.page_link("pages/tip_calculator.py", label="Day 2: Tip Calculator", icon="💸")
    st.page_link("pages/rock_paper_scissors.py", label="Day 4: Rock Paper Scissors", icon="✂️")
st.divider()

# Call to Action / Socials
st.info("🔗 **Let's connect:** If you want to see the raw code or just reach out, you can find me on [LinkedIn](https://www.linkedin.com/in/andreteaguejr/) and [GitHub](https://github.com/TypicalTeague).")