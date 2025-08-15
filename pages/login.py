import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv('.env')

st.set_page_config(
    layout='centered',
    page_title='Government Disbursement Schemes Assistant',
)

st.title('Login')

form = st.form(key='form')
password = form.text_input(label='Password', type='password')

if form.form_submit_button('Submit'):
    if password == os.getenv('APP_PASSWORD'):
      st.session_state.is_logged_in = True
      st.rerun()
    else:
      st.write('You have entered an incorrect password.')
