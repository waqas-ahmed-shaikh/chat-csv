import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import OpenAI
from langchain_groq import ChatGroq
from groq import Groq
from langchain.agents.agent_types import AgentType

def main():
    st.set_page_config(page_title='Ask your CSV')
    st.header("Ask your CSV")

    user_csv = st.file_uploader("Upload your CSV file", type='csv')

    if user_csv is not None:
        user_question = st.text_input('Ask a question about your CSV')

        llm = ChatGroq(model="mixtral-8x7b-32768", api_key='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')
        agent=create_csv_agent(llm, user_csv, verbose = True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)


if __name__ =="__main__":
    main()