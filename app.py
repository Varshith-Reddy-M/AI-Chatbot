import os
import time
import streamlit as st
from openai import OpenAI
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key,base_url="https://openrouter.ai/api/v1")
st.title("DevSenseAI")

if "chats" not in st.session_state:
    st.session_state.chats = {"Chat 1": []}
    st.session_state.current_chat = "Chat 1"

messages = st.session_state.chats[st.session_state.current_chat]

with st.sidebar:
    st.title("DevSenseAI ⚙️")
    if st.button("🧹 Clear Chat"):
      st.session_state.chats[st.session_state.current_chat] = []
      st.rerun()
    st.markdown("### About")
    st.write("AI assistant for coding help, explanations, and debugging.")
    st.write("Model: GPT-4o-mini (via OpenRouter)")
    st.title("Chats")
    if st.button("+ New Chat"):
        new_chat = f"Chat {len(st.session_state.chats) + 1}"
        st.session_state.chats[new_chat] = []
        st.session_state.current_chat = new_chat
    
    for chat in st.session_state.chats:
        if st.button(chat):
            st.session_state.current_chat = chat

for msg in messages:
    if msg["role"] == "user":
        st.write(f"👨‍💻 {msg['content']}")
    else:
        st.write(f"🤖 {msg['content']}")

user_input = st.chat_input("Ask your question:")

if user_input:
  prompt = user_input.lower()
  if "error" in prompt or "bug" in prompt or "debug" in prompt:
    content="You are an expert debugging assistant. Identify the error, explain why it occurs, and provide a clear fix with code if needed. Keep the explanation simple and structured."
  elif "code" in prompt:
    content="You are a helpful coding assistant for developers."
  elif "explain" in prompt:
    content="You are a teacher. Explain the concept clearly in simple terms with examples. Break it down step by step so a beginner can understand."
  else:
    content="You are a helpful coding assistant. Answer clearly and concisely, and provide examples when useful."

  messages.append({"role": "user", "content": user_input})

if user_input:
    st.chat_message("User",avatar="👨‍💻").write(user_input)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True
    )
    ph=st.chat_message("DevSenseAI",avatar="🤖").empty()
    ans=""
    for chunk in response:
        ans+=chunk.choices[0].delta.content
        ph.write(ans)
        time.sleep(0.01)