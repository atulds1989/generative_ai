import pathlib
import textwrap
import os
import streamlit as st

from IPython.display import display
from IPython.display import Markdown

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key=API_KEY)



def talk(input):
  model = genai.GenerativeModel('gemini-pro')
  chat = model.start_chat(history=[])
  response = chat.send_message(input)
  # text = to_markdown(response.text)

  # print(response.text)
  return response.text
  # return text

def footer():

    st.markdown("---")
    st.markdown("### About")
    st.markdown("This app recommends books based on user input and displays the top 10 popular books.")
    st.markdown("Developed by Your Name")


