from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit framework
st.title('Langchain Chatbot Demo With OPENAI and LLaMA3.1 APIs')

# Dropdown to select API
api_choice = st.selectbox("Select the API", ("OpenAI GPT-4o", "LLaMA3.1"))

# Input text
input_text = st.text_input("Enter Input")

# Initialize the LLM based on the user's choice
if api_choice == "OpenAI GPT-4o":
    llm = ChatOpenAI(model="gpt-4o")
elif api_choice == "LLaMA3.1":
    llm = Ollama(model="llama3.1")

# Output parser
output_parser = StrOutputParser()

# Chain prompt and LLM
chain = prompt | llm | output_parser

# Display the output
if input_text:
    st.write(chain.invoke({"question": input_text}))
