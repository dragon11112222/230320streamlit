import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
import os
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.title("Pokemon Graph")

df = pd.read_csv("pokemon5.csv", encoding="UTF-8")

col = df.columns.drop(["Unnamed: 0","pokedex_number","german_name","japanese_name"])
against_col = [i for i in df.columns if "against_" in i]
ability_col = [i for i in df.columns if "abili" in i]
is_col = [i for i in df.columns if "is_" in i]
col_xy = col.drop(against_col)
col_xy = col_xy.drop(ability_col)
col_xy = col_xy.drop(is_col)
col_xy = col_xy.drop('name')

objectory_info = ["type_1", "type_2"]

X_var = st.selectbox("X-axis", col_xy)
y_var = st.selectbox("Y-axis", col_xy)
z_var = st.selectbox('Color', col_xy)
# df1 = df.groupby("type1")[col].sum()
fig = px.scatter(df, x = X_var, y = y_var, color = z_var, hover_name = "name")
fig.update_traces(
    mode='markers',
    marker={'sizemode':'area',
            'sizeref':10})
fig.update_layout(
    template="simple_white",
    dragmode = 'zoom',
    #hovermode = "x unified",
    scattermode = "group",
    hoverlabel_namelength = 100,
    hoverlabel_font_size = 15
)
st.plotly_chart(fig,use_container_width = True)


# attack & defense
st.header('Attack & Defense')
fig = px.scatter(df, x='attack', y='defense', color='hp', hover_name='name')
st.plotly_chart(fig)

# weight & speed
st.header('Weight & Height')
fig = px.scatter(df, x='height_m', y='weight_kg', color='speed', hover_name='name')
st.plotly_chart(fig)