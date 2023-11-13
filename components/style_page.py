import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)

def show_style_page(openai_api_key):
    st.title("StyleSculpt - Code Style Checker")
    
    st.markdown('Ensure code quality and adherence to coding standards with StyleSculpt. This feature provides feedback on coding style, offering suggestions for improvement. By enforcing best practices, StyleSculpt enhances code quality and consistency.')

    with st.form(key="style_form"):
        refined_code = st.text_area("Enter refined code")

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            chat = ChatOpenAI(
                model="gpt-3.5-turbo-16k",
                openai_api_key=openai_api_key,
                temperature=0
            )
            system_template = """You are an AI assistant designed to provide real-time feedback on coding style and offer suggestions for improvement."""
            system_message_prompt = SystemMessagePromptTemplate.from_template(
                system_template)
            human_template = """Please provide feedback and suggestions for improving the coding style of the following code:

    {refined_code}"""
            human_message_prompt = HumanMessagePromptTemplate.from_template(
                human_template)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )

            chain = LLMChain(llm=chat, prompt=chat_prompt)
            result = chain.run(refined_code=refined_code)
            st.markdown(result)
