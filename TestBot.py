import streamlit as st
import random
import time

# Now it's safe to use st.markdown
st.markdown("""
<style>
    .chat-bubble {
        display: inline-block;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px;
        word-wrap: break-word;
        max-width: 70%;
    }
    .user-bubble {
        background-color: #d4f8d4;
        color: black;
        float: right;
        clear: both;
    }
    .bot-bubble {
        background-color: #d0e7ff;
        color: black;
        float: left;
        clear: both;
    }
</style>
""", unsafe_allow_html=True)
