import streamlit as st
import pandas as pd
import numpy as np

st.title("Layout")

st.markdown("---")


with st.echo():
    st.sidebar.write("sidebar test")
st.markdown("---")

with st.echo():
    a, b = st.columns(2)
    with b:
        st.write("col check, should be second column")

    with a:
        st.write("col check, should be first column")

    taba, tabb = st.tabs(["tab a", "tab b"])
    taba.write("tab a test")
    tabb.write("tab b test")

    with st.expander("open to see expander"):
        st.write("works!")

    container = st.container()

    container.write("should write in the container")

    placeholder = st.empty()

    placeholder.write("should write in the empty block")

    container.write("second line added")

    placeholder.write("replacement")

    container.markdown("---")
st.markdown("---")