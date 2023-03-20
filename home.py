import streamlit as st

st.set_page_config(
     page_title="SNU Fintech Course",
     page_icon="💵",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://gsds.snu.ac.kr',
         'About': "# This is a Streamlit Tutorials for SNU Fintech course"
     }
 )

st.header("Hello, Fintech!")

st.subheader("Streamlit Tutorials")

st.image("./static/img/fintech.jpeg", use_column_width=True)

