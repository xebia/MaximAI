from langchain_community.callbacks import StreamlitCallbackHandler
import streamlit as st
import requests


def chat_ui():

    if question := st.chat_input():
        st.chat_message("user").write(question)

        with st.chat_message("bear"):
            st_callback = StreamlitCallbackHandler(st.container())

            response = requests.post("http://localhost:8000/chat", json={"text": question, "user_id": "Emmy"}).json()
            st.write(response)


if __name__ == "__main__":
    chat_ui()

