import streamlit as st
from matching.matcher import get_best_answer

st.set_page_config(page_title="Art Studio Assistant", page_icon="🎨")
st.title("🎨 Art Studio Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask me about the studio..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    answer = get_best_answer(user_input)

    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})