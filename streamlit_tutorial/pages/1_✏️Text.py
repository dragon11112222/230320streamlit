import streamlit as st
import pandas as pd
import numpy as np

st.title("Writing Text")

st.markdown("---")


with st.echo():
    st.text('Fixed width text')
st.markdown("---")

with st.echo():
    st.markdown('_Markdown_')
st.markdown("---")

with st.echo():
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.markdown("---")

with st.echo():
    st.write('Most objects')
st.markdown("---")

with st.echo():
    st.write(['st', 'is <', 3])
st.markdown("---")

with st.echo():
    "this is magic"
    ['first', 'second', 'third']
    df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    df
st.markdown("---")


with st.echo():
    st.title('My title')
st.markdown("---")


with st.echo():
    st.header('My header')
st.markdown("---")

with st.echo():
    st.subheader("My sub")
st.markdown("---")


with st.echo():
    st.caption("hello caption")
st.markdown("---")


with st.echo():
    st.code('for i in range(8): foo()')
st.markdown("---")