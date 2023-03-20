import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Widgets")

st.markdown("---")


with st.echo():
    st.text_input("textbox")
st.markdown("---")

with st.echo():
    st.number_input("number")
st.markdown("---")

with st.echo():
    st.slider("slider")
st.markdown("---")

with st.echo():
    st.button("button")
st.markdown("---")

with st.echo():
    st.checkbox("checkbox")
st.markdown("---")

with st.echo():
    st.radio("radio", ["cat", "dog"])
st.markdown("---")


with st.echo():
    st.selectbox("selectbox", ["cat", "dog"])
st.markdown("---")


with st.echo():
    st.multiselect("multiselect", ["cat", "dog"])
st.markdown("---")

with st.echo():
    st.select_slider("select slider", ["cat", "dog"])
st.markdown("---")

with st.echo():
    st.text_area("text area")
st.markdown("---")

with st.echo():
    st.date_input("date input")
st.markdown("---")

with st.echo():
    st.time_input("time input")
st.markdown("---")

with st.echo():
    st.file_uploader("file input")
st.markdown("---")

with st.echo():
    st.color_picker("color picker")
st.markdown("---")

with st.echo():
    text_contents = """This is some text"""
    st.download_button("Download some text", text_contents)
st.markdown("---")

with st.echo():
    st.camera_input("cam input")
st.markdown("---")











