import pathlib
import textwrap
import os
from PIL import Image

from IPython.display import display
from IPython.display import Markdown

import google.generativeai as genai
from dotenv import load_dotenv

import numpy as np
import cv2, numpy as np
import pandas as pd 

import pickle, cv2
import streamlit as st 
import chat, gen_text_app, img_to_txt
import streamlit as st 


from streamlit_option_menu import option_menu


load_dotenv()

API_KEY = os.getenv("API_KEY")
st.header("Generative AI")

st.title("How may I help you")

with st.sidebar:
    
    selected = option_menu('Options',
                          
                          ['Ask a Question',
                           'Generate Text',
                           'Image to Text'],

                          icons=['robot', 'robot','robot'],

                          default_index=0)
    
    

if (selected == 'Ask a Question'):
    
    st.title('Ask a Question')
    input = st.text_input('Please enter the question you want to ask')
    submit = st.button('Answer')
    
    if submit:
        if not input:
            st.error("Please enter question")
        else:
            main_placeholder = st.empty()
            main_placeholder.text("Retrieving...Result...✅✅✅")

            data = chat.talk(input=input)
            if data:
                st.write("Your answer is : ",data)
                # main_placeholder.text(data)
    chat.footer()
    



if (selected == 'Generate Text'):
    
    st.title('Generate Text')
    input = st.text_input('Please enter the subject for which you want to generate text')

    submit = st.button('Generate')



    if submit:
        if not input:
            st.error("Please enter some text")
        else:
            main_placeholder = st.empty()
            main_placeholder.text("Retrieving...Result...✅✅✅")
            
            data = gen_text_app.text_generation(input=input)
            if data:
                    st.write("Your answer is : ",data)
                    # main_placeholder.text(data)


                     
    chat.footer()
    

if (selected == 'Image to Text'):
    
    st.title('Image to Text')
    st.write('Please upload an image')
    input = st.file_uploader("upload in jpg format",type="jpg")
    submit = st.button('Generate')

    if submit:
        if input:
            main_placeholder = st.empty()
            main_placeholder.text("Retrieving...Result...✅✅✅")

            img = Image.open(input)
            model = genai.GenerativeModel('gemini-pro-vision')
            response = model.generate_content(img)
            text = response.text
            st.write(text)
            # main_placeholder.text(text)
            

        else:
                st.error("please upload an image")
    # else:
    #     st.error("please upload an image")
                     
    chat.footer()
    
