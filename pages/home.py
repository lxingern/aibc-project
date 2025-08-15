import streamlit as st
from logic import query_handler

if 'is_logged_in' not in st.session_state or not st.session_state.is_logged_in:
    st.switch_page('pages/login.py')

st.set_page_config(
    layout='centered',
    page_title='Government Disbursement Schemes Assistant',
)

st.title('Government Disbursement Schemes Assistant')

form = st.form(key='form')
form.subheader('Ask me anything about government disbursement schemes!')

query = form.text_area('Enter your query here.', height=100)

if form.form_submit_button('Submit'):
    st.toast('Query submitted!')
    response = query_handler.process_user_query(query)
    st.write(response)
