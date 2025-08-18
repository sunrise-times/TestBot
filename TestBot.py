import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Intel AI Chatbot", layout="centered")

# Title
st.markdown("<h2 style='text-align: center;'>Intel AI Chatbot 🤖</h2>", unsafe_allow_html=True)
st.write("Ask a question related to Intel processors or support.")

# Instructions dictionary
instructions = {
    ("hello", "hi"): [
        "Intel AI: Hello, how can I help you?",
        "Intel AI: Hi there, what's on your mind?",
        "Intel AI: Hello, I am here to assist"
    ],
    ("hot", "overheat", "temperature", "high"): [
        ("Intel AI: I will look for this, if you can tell me whether the processor used is NUC, "
         "box, or tray")
    ],
    ("nuc",): [
        """Intel AI: Customer Support Services for Intel NUC Products Has Transitioned to ASUS as of January 16, 2024. 
           For more details refer to article: 000097279"""
    ],
    ("tray", "laptop"): [
        "Intel AI: Send customer to system manufacturer as we do not handle laptop or pre-built systems"
    ],
    ("box", "desktop"): [
        "Intel AI: Can you give me a complete model number of the processor?"
    ],
    ("13900k", "14900", "intelcore", "ultra", "235a"): [
        "Intel AI: Suggest customer to check:\n"
        "- The thermal solution\n"
        "- Check fan operation status\n"
        "- Load BIOS to default or Update BIOS\n"
        "For more troubleshooting steps refer to article: 000005791"
    ],
    ("Intel", "Core", "i5", "3450", "Processor"): [
        "Intel AI: Oh oh! This is an EOIS product, suggest customer to post in Intel community forum"
    ]
}

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("Ask Intel AI:")

# Process input
if user_input:
    x = user_input.lower().strip()
    words = x.split()

    if x in ("ok bye", "exit", "quit"):
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", "Intel AI: Goodbye! Take care."))
    else:
        found = False
        for keywords, reply_list in instructions.items():
            if any(word in keywords for word in words):
                response = random.choice(reply_list)
                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("bot", response))
                found = True
                break
        if not found:
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("bot", "Intel AI: Sorry, I did not understand. Can you provide more details?"))

# Display chat bubbles
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"<div style='text-align: right; background-color: #DCF8C6; padding: 10px; border-radius: 10px; margin: 5px;'>{message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #F1F0F0; padding: 10px; border-radius: 10px; margin: 5px;'>{message}</div>", unsafe_allow_html=True)
