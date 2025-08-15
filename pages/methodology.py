import streamlit as st

st.set_page_config(
    layout='centered',
    page_title='Government Disbursement Schemes Assistant',
)

st.title('Methodology')

st.header('Data Flow')
st.image('Data flow.png')

st.header('Implementation Considerations')
st.write("One of the decisions I had to make was whether to load content from all the web pages for all the schemes upfront, or only load content from pages on a specific scheme once that scheme is identified from the user's query (i.e. on demand). I decided on the latter, as loading all the pages on app initiation would take some time. This approach would also ensure that the information used to reply the query is up-to-date. Furthermore, the projected traffic of this app is still low, so it would be unnecessary to load all the pages when only a few users would be using it. However, this means that the user would have to wait longer for a response to their query as the app would need to load the content of the web pages before constructing a response. If this app were to have wider usage, then loading everything upfront might be a better idea. The web pages are unlikely to be updated frequently, so there is less of a concern that the information is outdated.")

st.write("Another drawback of this app is that the mapping of the scheme to the web page links is currently hardcoded in the app. As far as I can tell, the links are not predictable enough that they can be constructed dynamically. Hence if there are any changes to the links, they would have to be updated manually. Maybe there is a way for the LLM to find these links on its own, but currently I don't have the knowledge to implement it.")

