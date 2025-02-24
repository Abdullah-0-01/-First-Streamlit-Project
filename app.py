#  to install stremlit we use pip install stremlit

import streamlit as st
import random

def get_random_quote():
    quotes = [
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "Do not be embarrassed by your failures, learn from them and start again. - Richard Branson",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Effort is what ignites that ability and turns it into accomplishment. - Carol Dweck",
        "Your mindset matters. It affects everything—from the business you run to the relationships you have. - Carol Dweck"
    ]
    return random.choice(quotes)

st.title("🌱 Growth Mindset Guide")

# Motivational Quote
st.subheader("💡 Daily Motivation")
st.write(get_random_quote())

# Growth Mindset vs. Fixed Mindset
st.subheader("🧠 Growth vs. Fixed Mindset")
st.write("""
A **Growth Mindset** means you believe your intelligence and abilities can be developed with effort and persistence. A **Fixed Mindset**, on the other hand, assumes intelligence and talent are static.

**Growth Mindset Characteristics:**
- Embraces challenges
- Persists through obstacles
- Sees effort as a path to mastery
- Learns from criticism
- Finds lessons in others' success

**Fixed Mindset Characteristics:**
- Avoids challenges
- Gives up easily
- Sees effort as fruitless
- Ignores useful feedback
- Feels threatened by others' success
""")

# Tips for Developing a Growth Mindset
st.subheader("📌 Tips to Develop a Growth Mindset")
st.write("""
1. Embrace Challenges: Step out of your comfort zone.
2. Learn from Mistakes: Failure is a stepping stone to success.
3. Keep Learning: Stay curious and open-minded.
4. Take Feedback Positively: See criticism as an opportunity to grow.
5. Stay Persistent: Don't give up easily, keep pushing forward.
""")

# Interactive: What's Your Growth Mindset Score?
st.subheader("📊 Growth Mindset Self-Check")
score = st.slider("On a scale of 1-10, how much do you believe you can improve your abilities with effort?", 1, 10, 5)
if score > 7:
    st.success("Great! You already have a strong growth mindset! Keep pushing forward! 🚀")
elif score > 4:
    st.info("You're on the right path! Keep practicing a growth mindset daily. 🌟")
else:
    st.warning("It's time to embrace challenges and see failures as learning opportunities! 💪")

st.write("---")
st.write("🚀 *Keep growing, keep learning!*")

