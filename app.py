import streamlit as st

st.set_page_config(page_title="Saurabh AI chartboat", page_icon="💬", layout="centered")

from aichart import webfun


st.markdown("""
    <style>
        .sidebar .sidebar-content {
            padding-top: 10px;
        }
        .sidebar radio {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            text-align: center;
            display: inline-block;
            font-size: 16px;
            margin: 20px;
            cursor: pointer;
            border-radius: 5px;
            border: none;
            width: 100%;
        }
        .sidebar button:hover {
            background-color: #45a049;
        }
        .main-content {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .main-content h1 {
            color: #333;
        }
        .main-content p {
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Navigation Menu", ("About", "Chat with me", "Instruction"))

if page == "About":
    st.markdown('<h1 class="center-title">About Saurabh Jha AI Chatbot</h1>', unsafe_allow_html=True)
    st.write("""
    Welcome to **Saurabh Jha AI Chatbot**, my personal AI assistant designed to answer any questions you have!
    - 🌟 **Smart AI** powered by **RAG architecture** for accurate and context-aware answers.
    - 🚀 **Fast & Accurate** responses to your questions.
    - 💬 **Easy to Use** – Just ask a question and get instant replies.
    """)
elif page == "Instruction":
    st.markdown('<h1 class="center-title">Instructions</h1>', unsafe_allow_html=True)
    st.write("""
    - **Step 1:** Choose "Chat with me" to start chatting.
    - **Step 2:** Type your question in the input box.
    - **Step 3:** Receive an AI-generated response instantly.
    """)
    st.markdown("### ⚠️ Important: LLM API Usage Limit")
    st.write("""
    - I have a limit of **100 API calls per month**.
    - Please **ask only necessary and important questions**.
    - Keep your questions **short, clear, and specific**.
    - Avoid unnecessary or repetitive queries to **save API calls**.
    """)
    
elif page == "Chat with me":
    try:
        webfun()
    except Exception:
        st.error("⚠️ Something went wrong. Please try again later.")




