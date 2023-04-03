import streamlit as st
from PIL import Image

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

st.header("Pokemon Visualization : All about Pokemon")

st.subheader("SNU Bigdata Fintech course 2조")

st.write('고현수 남윤재 문소현 윤지영 이건준 정세용')


image = Image.open("image/Pigeon.jpeg")
st.image(image,width = 320)
