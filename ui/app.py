import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from matching.matcher import get_best_answer

st.set_page_config(page_title="Art Studio Assistant", page_icon="🎨")
st.title("🎨 Art Studio Chatbot")
st.caption("Ask me anything about classes, pricing, hours, and more.")

# Welcome message on first load
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm the Art Studio assistant 🎨 Ask me about our classes, opening hours, pricing, or anything else!"
        }
    ]

# Redraw chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Suggested questions
st.markdown("**Quick questions:**")
cols = st.columns(3)
suggestions = [
    "What classes do you offer?",
    "How much does a class cost?",
    "Where are you located?",
]
for i, suggestion in enumerate(suggestions):
    if cols[i].button(suggestion):
        st.session_state.messages.append({"role": "user", "content": suggestion})
        answer = get_best_answer(suggestion)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

# Chat input
if user_input := st.chat_input("Ask me about the studio..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    answer = get_best_answer(user_input)

    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})