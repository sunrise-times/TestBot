import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="Infinity Copilot", layout="centered")

# Custom CSS for chat bubbles and light theme
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            color: black;
            font-family: 'Segoe UI', sans-serif;
        }
        .chat-bubble {
            padding: 10px 15px;
            border-radius: 15px;
            margin: 8px 0;
            max-width: 80%;
            word-wrap: break-word;
        }
        .user-bubble {
            background-color: #d4f8d4;
            color: black;
            margin-left: auto;
            text-align: right;
        }
        .bot-bubble {
            background-color: #d0e7ff;
            color: black;
            margin-right: auto;
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

def get_response(message):
    message = message.lower().strip()
    if message in ("exit", "quit", "ok bye"):
        return "Goodbye! Take care."

    words = message.split()
    for keywords, replies in instructions.items():
        if any(word in keywords for word in words):
            return random.choice(replies)

    return "Sorry, I did not understand. Can you provide more details?"

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.markdown("<h2 style='text-align:center;'>Infinity Copilot</h2>", unsafe_allow_html=True)

# Display chat history with bubbles
for sender, msg in st.session_state.chat_history:
    bubble_class = "user-bubble" if sender == "You" else "bot-bubble"
    st.markdown(f"<div class='chat-bubble {bubble_class}'><strong>{sender}:</strong> {msg}</div>", unsafe_allow_html=True)

# Input
user_input = st.text_input("Ask Infinity...", key="input")

# Send button
if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append(("You", user_input))
        response = get_response(user_input)

        # Simulate typing effect
        typing_placeholder = st.empty()
        typed_text = ""
        for char in response:
            typed_text += char
            typing_placeholder.markdown(
                f"<div class='chat-bubble bot-bubble'><strong>Infinity:</strong> {typed_text}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.02)

        typing_placeholder.empty()
        st.session_state.chat_history.append(("Infinity", response))
        st.session_state.input = ""
        st.experimental_rerun()

# Restart
