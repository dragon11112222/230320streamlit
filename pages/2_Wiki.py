import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
import os
import numpy as np
import plotly.graph_objects as go


st.header("Pokemon Wikipedia")

df = pokemon = pd.read_csv("pokemon2.csv", encoding="cp949")
#df = df.drop(df[df.korean_name == '야도킹'].index).reset_index(drop=True)
df = df.iloc[:721]
columns = ['attack', 'hp', 'defense', 'sp_attack', 'sp_defense', 'speed']
# df = pokemon[columns].copy()

# # Normalize data for better readability
# normalized_df = (df - df.min()) / (df.max() - df.min())

name_selected = st.selectbox("Pokemon", list(df.korean_name))
name_selected_index = df.index[df.korean_name == name_selected].tolist()[0]



def radar_chart1(pokemon_1_index):
    '''
    Print radarchart of two pokemons
    pokemon_1_index: int, index of pokemon in 'normalized_df'
    pokemon_2_index: int, index of pokemon in 'normalized_df'
    '''

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        #r=df.loc[pokemon_1_index,:].tolist(),
        r=df.loc[pokemon_1_index, columns],
        theta=columns,
        fill='toself',
        name=pokemon.loc[pokemon_1_index, 'korean_name']
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                
                #range=[0, 10 + max(df.loc[pokemon_1_index]['hp'], df.loc[pokemon_1_index]['attack'],
                #                   df.loc[pokemon_1_index]['defense'], df.loc[pokemon_1_index]['sp_attack'],
                #                   df.loc[pokemon_1_index]['sp_defense'], df.loc[pokemon_1_index]['speed'])]
                
                range = [0, 200]
            )),
        showlegend=False
    )

    fig.update_layout(
        title="Radar Chart: " + pokemon.loc[pokemon_1_index, 'korean_name'])

    st.plotly_chart(fig)



image_dir = 'images/'
def image_allocating(df, image_dir, image_type = '.jpg', new_column = "image",length = 721):

    image_files = [f for f in os.listdir(image_dir) if f.endswith(image_type)]

    df = df.iloc[:length]
    #sorted_files = sorted(image_files, key = lambda x: int(x.split('.')[0].split('-')[0].split('f')[0]))
    sorted_files = sorted(image_files, key = lambda x: int(x.split('.')[0]))
    df[new_column] = sorted_files
    return df



df = image_allocating(df =df, image_dir = image_dir)
df.drop(columns = "japanese_name", inplace = True)
super1, super2 = st.columns(2)
# super1 = st.columns(1)

with super1:
    # for i in range(0, 50):
        col1, col2 = st.columns([4, 3])
        with col1:
            st.text("No.0"+str(name_selected_index+1))
            image = Image.open(image_dir+df['image'][name_selected_index])
            st.image(image, width = 320 )
        with col2:
            st.text("Pokemon Information")
            st.markdown(f"""이름: {df["korean_name"][name_selected_index]}
                        <br>
                        <br>
                        공격: {df["attack"][name_selected_index]}
                        <br>
                        방어: {df["defense"][name_selected_index]}
                        <br>
                        HP: {df["hp"][name_selected_index]}
                        <br>
                        SP공격: {df["sp_attack"][name_selected_index]}
                        <br>
                        SP방어: {df["sp_defense"][name_selected_index]}
                        <br>
                        속도: {df["speed"][name_selected_index]}
                        <br>
                        <br>
                        Type1: {df["type1"][name_selected_index]}
                        <br>
                        Type2: {df["type2"][name_selected_index]}
                        <br>
                        세대: {df["generation"][name_selected_index]}
                        """, unsafe_allow_html=True)
        # with col3:
            # radar_chart1(pokemon_1_index=200)

with super2:
    # for i in range(0, 50):
        radar_chart1(pokemon_1_index = name_selected_index)
