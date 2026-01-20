import streamlit as st
import random
import time

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(
    page_title="🤯 Interesting Facts",
    page_icon="🌍",
    layout="centered"
)

# -----------------------------
# Data
# -----------------------------
FACTS = {
    "🌌 Space": [
        "A day on Venus is longer than a year on Venus.",
        "There are more stars in the universe than grains of sand on Earth.",
        "Neutron stars are so dense that a teaspoon of one would weigh about a billion tons.",
        "Saturn could float in water if you could find a bathtub big enough."
    ],
    "🧠 Human Body": [
        "Your brain uses about 20% of your body’s total energy.",
        "Humans share about 60% of their DNA with bananas.",
        "Your stomach gets a new lining every 3–4 days.",
        "The human nose can remember around 50,000 different scents."
    ],
    "🐙 Animals": [
        "Octopuses have three hearts and blue blood.",
        "Cows have best friends and get stressed when separated.",
        "A group of flamingos is called a flamboyance.",
        "Wombat poop is cube-shaped."
    ],
    "🌍 Earth": [
        "Earth isn’t perfectly round — it’s slightly squished.",
        "There are more trees on Earth than stars in the Milky Way.",
        "Hot water can freeze faster than cold water (Mpemba effect).",
        "Earth’s inner core is as hot as the surface of the Sun."
    ],
    "🤖 Technology": [
        "The first computer bug was an actual moth.",
        "More computing power exists in a smartphone than in NASA during the Moon landing.",
        "Email existed before the World Wide Web.",
        "The password for the first computer was literally 'password'."
    ]
}

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚙️ Settings")
category = st.sidebar.selectbox(
    "Choose a category",
    list(FACTS.keys())
)

auto_mode = st.sidebar.checkbox("🔄 Auto-generate facts")
delay = st.sidebar.slider("⏱️ Auto mode delay (seconds)", 2, 10, 4)

# -----------------------------
# Main UI
# -----------------------------
st.title("🤯 Interesting Facts Explorer")
st.markdown(
    "Discover **mind-blowing**, **fun**, and **unexpected** facts from different domains!"
)

st.divider()

# Session state for fact
if "fact" not in st.session_state:
    st.session_state.fact = random.choice(FACTS[category])

# Button
if st.button("🎲 Give me a fact"):
    st.session_state.fact = random.choice(FACTS[category])

# Display Fact
st.subheader(f"Category: {category}")
st.success(st.session_state.fact)

# Auto Mode
if auto_mode:
    with st.spinner("Generating awesome facts..."):
        time.sleep(delay)
        st.session_state.fact = random.choice(FACTS[category])
        st.experimental_rerun()

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("✨ Built with Streamlit | Facts make brains happy")
