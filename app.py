#  to install stremlit we use pip install stremlit

import streamlit as st
import random
import time

def get_random_quote():
    quotes = [
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "Do not be embarrassed by your failures, learn from them and start again. - Richard Branson",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Effort is what ignites that ability and turns it into accomplishment. - Carol Dweck",
        "Your mindset matters. It affects everything—from the business you run to the relationships you have. - Carol Dweck"
    ]
    return random.choice(quotes)

def progress_bar():
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    st.success("Mindset Boost Complete! ✅")

st.set_page_config(page_title="Growth Mindset Hub", layout="wide")
st.title("🚀 Growth Mindset Hub")

# Motivational Quote
st.subheader("💡 Daily Motivation")
st.info(get_random_quote())

# Growth Mindset vs. Fixed Mindset
st.subheader("🧠 Growth vs. Fixed Mindset")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Growth Mindset")
    st.success("""
    - Embraces challenges
    - Persists through obstacles
    - Sees effort as a path to mastery
    - Learns from criticism
    - Finds lessons in others' success
    """)

with col2:
    st.markdown("### Fixed Mindset")
    st.error("""
    - Avoids challenges
    - Gives up easily
    - Sees effort as fruitless
    - Ignores useful feedback
    - Feels threatened by others' success
    """)

# Tips for Developing a Growth Mindset
st.subheader("📌 Tips to Develop a Growth Mindset")
st.markdown("""
1. **Embrace Challenges** – Step out of your comfort zone.
2. **Learn from Mistakes** – Failure is a stepping stone to success.
3. **Keep Learning** – Stay curious and open-minded.
4. **Take Feedback Positively** – See criticism as an opportunity to grow.
5. **Stay Persistent** – Don't give up easily, keep pushing forward.
""")

# Interactive: Growth Mindset Self-Assessment
st.subheader("📊 Growth Mindset Self-Assessment")
score = st.slider("On a scale of 1-10, how much do you believe you can improve your abilities with effort?", 1, 10, 5)
if score > 7:
    st.success("Great! You already have a strong growth mindset! Keep pushing forward! 🚀")
elif score > 4:
    st.info("You're on the right path! Keep practicing a growth mindset daily. 🌟")
else:
    st.warning("It's time to embrace challenges and see failures as learning opportunities! 💪")

# Interactive Exercise
st.subheader("🚀 Mindset Boost Challenge")
if st.button("Start a Mindset Boost Session"):
    progress_bar()

st.write("---")
st.write("🌟 *Keep growing, keep learning, and unlock your full potential!* 🌟")
