import streamlit as st
import pandas as pd
import os

from langchain_openai import OpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

st.set_page_config(page_title="Ask Anything", page_icon="🤖")
st.title("🤖 Ask a Question About EPL Stats")

# Load the EPL dataset
df = pd.read_csv("epl_player_stats_24_25.csv")

# Secure API key input
api_key = st.text_input("Enter your OpenAI API key", type="password")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

    # Load LLM and agent
    llm = OpenAI(temperature=0)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    # Ask a question
    question = st.text_input("Ask your question:")

    if st.button("Ask") and question:
        with st.spinner("Thinking... 🤔"):
            try:
                response = agent.run(question)
                st.success("Answer:")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.warning("🔐 Please enter your OpenAI API key to use this feature.")