import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Display")

st.markdown("---")


with st.echo():
    df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.dataframe(df)
    st.table(df)
    st.metric("Metric", 42, -2)
st.markdown("---")

with st.echo():
    image_nums = np.random.randint(255, size=(144, 144), dtype=np.uint8)
    st.image(image_nums)
st.markdown("---")

with st.echo():
    sample_rate = 44100  # 44100 samples per second
    seconds = 2  # Note duration of 2 seconds
    frequency_la = 440  # Our played note will be 440 Hz
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * sample_rate, False)
    # Generate a 440 Hz sine wave
    note_la = np.sin(frequency_la * t * 2 * np.pi)

    st.audio(note_la, sample_rate=sample_rate)
    st.video("https://youtu.be/RjiqbTLW9_E")
st.markdown("---")








