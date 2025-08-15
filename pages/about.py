import streamlit as st

st.set_page_config(
    layout='centered',
    page_title='Government Disbursement Schemes Assistant',
)

st.title('About Us')
st.write("The Government Disbursement Schemes Assistant is a simple application that aims to answer citizens' queries on government disbursement schemes based on the latest available information.")

st.header('Features')
st.write('On receiving a query, the Assistant uses RAG (Retrieval Augmented Generation) to accurately respond to it. Based on the scheme in question, it scrapes content directly from government website pages to obtain the latest information to inform its response.')
st.write('There are also security measures in place to prevent prompt injection or otherwise inappropriate usage of the Assistant.')

st.header('Data Sources')
st.write('The Assistant uses pages from the government website https://www.govbenefits.gov.sg as data sources. The Assistant identifies the scheme that the user is asking about, then scrapes content from the relevant pages.')
st.write('E.g. if the user is asking about the GST Voucher, the Assistant will look at pages on the GST Voucher, such as https://www.govbenefits.gov.sg/about-us/gst-voucher/overview/ and https://www.govbenefits.gov.sg/about-us/gst-voucher/am-i-eligible/.')