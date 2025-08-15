import streamlit as st

if 'is_logged_in' not in st.session_state or not st.session_state.is_logged_in:
    pages = [
        st.Page('pages/login.py', title='Login', default=True),
    ]
else:
    pages = [
        st.Page('pages/home.py', title='Home', default=True),
        st.Page('pages/about.py', title='About'),
        st.Page('pages/methodology.py', title='Methodology'),
    ]

# pages = [
#     st.Page('pages/home.py', title='Home', default=True),
#     st.Page('pages/about.py', title='About'),
#     st.Page('pages/methodology.py', title='Methodology'),
#     st.Page('pages/login.py', title='Login'),
# ]

pg = st.navigation(pages, position='top')

pg.run()