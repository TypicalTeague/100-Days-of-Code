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

st.divider()

# Call to Action / Socials
st.info("🔗 **Let's connect:** If you want to see the raw code or just reach out, you can find me on [LinkedIn](https://www.linkedin.com/in/andreteaguejr/) and [GitHub](https://github.com/TypicalTeague).")