import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
f = open("keys/.gemini_api_key.txt")
key = f.read()
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Set Streamlit page configuration
st.set_page_config(
    page_title="AI Data Science Tutor",
    page_icon="📊",
    layout="wide"
)

# Check for messages in session and create a title if not exists
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I'm your Data Science Tutor. How can I assist you with your data science queries today?"}
    ]
    st.title(":chart_with_upwards_trend: [AI Data Science Tutor]")

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Receive user input
user_input = st.chat_input("")

# Store user input in session
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

# Generate AI response and display
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = model.generate_content(user_input)
            st.write(ai_response.text)
    new_ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(new_ai_message)