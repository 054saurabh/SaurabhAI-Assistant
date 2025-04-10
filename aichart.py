import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

st.markdown("""
    <style>
        .main-content {
            position: absolute;
            top: 6px;
            width: 96%;
            height: 100px;
            background-color: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            margin: auto;
            display: flex;
            justify-content: center;
            align-items: center;
            
        }

        .main-content h1 {
            font-size: 20px;
            color: #333;
        }
    </style>
    """, unsafe_allow_html=True)

def sayAI(query):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,
        index_name="faiss"
    )

    retriever = vectorstore.as_retriever()
    search_results = retriever.invoke(query)

    prompt = ChatPromptTemplate.from_template("""
        You are Saurabh Kumar Jha's official AI representative. Your purpose is to professionally and accurately share 
        information about Saurabh's background, skills, and experience with recruiters and professional contacts. Always 
        maintain a tone that is helpful, precise, and reflects well on Saurabh's professional brand.

        Previous Conversations:
        {chat_history}

        Context:
        {search_results}

        Question: {query}

        Response Rules:
        1. Identity: Always begin by identifying yourself: "I'm Saurabh Kumar Jha's AI assistant."
        2. Accuracy: Only use information from the provided context. Never guess or assume. If uncertain: 
           "I don't have that specific information about Saurabh, but his [related skill/experience] might be relevant."
        3. Handling Unknowns:
           - "That detail isn't in my records, but Saurabh would be happy to provide it if you connect with him directly."
           - "I specialize in Saurabh's professional background. Could you clarify which aspect you're interested in?"
        4. Value-Add: Where possible, connect questions to Saurabh's strengths:
           - "While I don't have those specifics, Saurabh's expertise in [relevant area] might address your needs."
        5. Closing: End positively when appropriate:
           - "Let me know if you'd like any other details about Saurabh's qualifications!"
           - "I hope this helps with your inquiry about Saurabh's background."

        Now please answer this question about Saurabh Kumar Jha: '{query}'
    """)

    memory = ConversationBufferWindowMemory(
        k=3, memory_key="chat_history", return_messages=True, input_key="query"
    )

    chain = LLMChain(llm=llm, memory=memory, prompt=prompt)
    response = chain.invoke({"query": query, "search_results": search_results})

    return response['text']

def webfun():
    st.markdown("<div class='main-content'><h1>Saurabh AI Chatbot – Personal AI Assistant</h1></div>", unsafe_allow_html=True)
    user_input = st.text_area("Ask your question!", height=100)
    if st.button("Submit", key="submit_button"):
        if user_input:
            user_input1=sayAI(user_input)
            response = f"You asked: {user_input}.\n\n🤖: {user_input1}"
        else:
            response = "Please enter a question to know more about Saurabh Kumar Jha."
    
        st.markdown(f'<div class="response">{response}</div>', unsafe_allow_html=True)
