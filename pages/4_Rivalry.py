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


st.header("기존의 상성표")
image = Image.open("image/against.png")
st.image(image, width = 640)

df = pd.read_csv("pokemon5.csv", encoding="UTF-8")
df = df.drop(df[df.name == '야도킹'].index).reset_index(drop=True)


image_dir = 'new_img/'
def image_allocating(df, image_dir, image_type='.jpg', new_column="image", length=819):
    image_files = [f for f in os.listdir(image_dir) if f.endswith(image_type)]

    df = df.iloc[:length]
    sorted_files = sorted(image_files, key=lambda x: int(x.split('-')[0].split('.')[0].split('f')[0]))
    return df


df = image_allocating(df=df, image_dir=image_dir)
col = df.columns.drop(["Unnamed: 0", "pokedex_number", "german_name", "japanese_name"])
against_col = [i for i in df.columns if "against_" in i]
# objectory_info = ["type_1", "type_2"]


st.header('상성표 개선')
# X_var = st.selectbox("타입 입력", objectory_info)
y_var = st.selectbox("상대방 type", against_col)
# df1 = df.groupby("type1")[col].sum()
fig = px.scatter(df, x='type_1', y="type_2", color=y_var, hover_name=y_var)

fig.update_traces(
    mode='markers',
    marker={'sizemode': 'area',
            'sizeref': 10})

fig.update_layout(

    template="simple_white",
    dragmode='zoom',
    # hovermode = "x unified",
    scattermode="group",
    hoverlabel_namelength=100,
    hoverlabel_font_size=15

)

st.plotly_chart(fig, use_container_width=True)


# details
st.header('상성표 세부')
type1_selected = st.selectbox("나의 type", list(set(df.type_1)))
fig4 = px.bar(df[df.type_1 == type1_selected], x='type_2', y=y_var, barmode="overlay", hover_name='name')
fig4.update_layout(

    template="simple_white",
    dragmode='zoom',
    # hovermode = "x unified",
    hoverlabel_namelength=20,
    hoverlabel_font_size=15

)
st.plotly_chart(fig4, use_container_width=True)