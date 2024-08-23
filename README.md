# Langchain Streamlit Demo with OpenAI and llama3 APIs

This project is a simple Streamlit-based web application that allows users to interact with language models using Langchain. Users can choose between OpenAI's GPT-4o and the LLaMA3.1 model powered by the Ollama API. 

## Features

- **API Selection**: Users can select either the OpenAI GPT-4o or LLaMA3.1 model.
- **Interactive Interface**: The app provides a text input for users to ask questions and get responses from the selected language model.
- **Seamless Integration**: Uses Langchain to integrate and process prompts through different LLMs.

## Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:Akash-K11/ChatBot-Langchain.git
    cd ChatBot-Langchain
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following variables:

    ```
    OPENAI_API_KEY=your_openai_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key
    ```

## Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Open your browser** and go to `http://localhost:8501` to use the application.

3. **Select the API** from the dropdown menu, enter your query in the text input, and hit enter to get a response from the selected model.