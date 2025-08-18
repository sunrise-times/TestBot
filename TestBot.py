import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Infinity Copilot", layout="centered")

# Custom CSS for Copilot-like look
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextInput > div > input {
            background-color: #2e2e2e;
            color: white;
            border: 1px solid #444;
            border-radius: 6px;
        }
        .stButton > button {
            background-color: #444;
            color: white;
            border-radius: 6px;
        }
        .message {
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .user {
            background-color: #3a3a3a;
            text-align: right;
        }
        .bot {
            background-color: #2e2e2e;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

# Chatbot logic
instructions = {
    ("hello", "hi"): [
        "Hello, how can I help you?",
        "Hi there, what's on your mind?",
        "Hello, I am here to assist"
    ],
    ("hot", "overheat", "temperature", "high"): [
        "I will look for this, if you can tell me whether the processor used is NUC, box, or tray"
    ],
    ("nuc",): [
        "Customer Support Services for Intel NUC Products Has Transitioned to ASUS as of January 16, 2024. For more details refer to article: 000097279"
    ],
    ("tray", "laptop"): [
        "Send customer to system manufacturer as we do not handle laptop or pre-built systems"
    ],
    ("box", "desktop"): [
        "Can you give me a complete model number of the processor?"
    ],
    ("13900k", "14900", "intelcore", "ultra", "235a"): [
        "Suggest customer to check:\n- The thermal solution\n- Check fan operation status\n- Load BIOS to default or Update BIOS\nFor more troubleshooting steps refer to article: 000005791"
    ],
    ("Intel", "Core", "i5", "3450", "Processor"): [
        "Oh oh! This is an EOIS product, suggest customer to post in Intel community forum"
    ]
}

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat response logic
def get_response(message):
    message = message.lower().strip()
    if message in ("exit", "quit", "ok bye"):
        return "Goodbye! Take care."

    words = message.split()
    for keywords, replies in instructions.items():
        if any(word in keywords for word in words):
            return random.choice(replies)

    return "Sorry, I did not understand. Can you provide more details?"

# Title
st.markdown("<h2 style='text-align:center;'>Infinity Copilot</h2>", unsafe_allow_html=True)

# Chat display
for sender, msg in st.session_state.chat_history:
    css_class = "user" if sender == "You" else "bot"
    st.markdown(f"<div class='message {css_class}'><strong>{sender}:</strong> {msg}</div>", unsafe_allow_html=True)

# Input form
with st.form("chat_form"):
    user_input = st.text_input("Ask Infinity...", "")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        response = get_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Infinity", response))
        st.experimental_rerun()

# Restart button
if st.button("🔄 Restart Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()
