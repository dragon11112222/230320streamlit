import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Etc")

st.markdown("---")


with st.echo():
    my_bar = st.progress(0)
    
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

    with st.spinner("Wait!"):
        time.sleep(5)
        st.write("done")
st.markdown("---")

with st.echo():
    st.error("st error")
    st.warning("st warning")
    st.info("st info")
    st.success("st success")
    e = RuntimeError("example of error")
    st.exception(e)
st.markdown("---")


