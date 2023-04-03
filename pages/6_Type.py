import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# reading dataset
df = pd.read_csv("pokemon5.csv", encoding='UTF-8')
df = df.drop(df[df.name == '야도킹'].index).reset_index(drop=True)
# print(len(df))



# stat & type
st.header('Type별 스탯 규모')
# non_legendary = df[df['is_legendary'] == 0]
means = df.groupby(['type_1'])[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].mean().reset_index()
# Melt the dataframe to create long format data
means_melted = pd.melt(means, id_vars=['type_1'], var_name='attribute', value_name='mean')
fig = px.treemap(means_melted, path=['type_1', 'attribute'], values='mean',
                 color='mean', color_continuous_scale='Viridis',
                 title='Mean Attributes by Type of Non-Legendary Pokemon',
                 hover_data={'type_1': True, 'attribute': True, 'mean': ':.1f'})
fig.update_layout(
    font_family='Arial',
    font_color='black',
    title_font_size=30,
    title_font_family='Arial',
    title_font_color='black',
    title_x=0.5,
    margin=dict(l=0, r=0, t=70, b=0),
    coloraxis_colorbar=dict(
        title_font_family='Arial',
        title_font_color='black',
        title='Mean Value',
        tickfont_family='Arial',
        tickfont_color='black',
        ticksuffix='%',
        lenmode='fraction',
        len=0.4,
        yanchor='middle',
        y=0.5,
        thickness=10,
        tickmode='auto',
        nticks=10
    )
)
st.plotly_chart(fig)


st.header('Type별 스탯 규모 Detail')
type1_selected = st.selectbox("나의 type", list(set(df.type_1)))

tab1, tab2 = st.tabs([ "🗃 Bar","📈 Chart"])

tab1.subheader('Bar chart')
fig = px.bar(means_melted[means_melted.type_1 == type1_selected], x = 'attribute', y = 'mean')
tab1.plotly_chart(fig)

tab2.subheader('Radar Chart')
fig = go.Figure()
fig.add_trace(go.Scatterpolar(theta= list(means_melted[means_melted.type_1 == type1_selected]['attribute']),
                              r= list(means_melted[means_melted.type_1 == type1_selected]['mean']),
                              fill= 'toself'))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 150]
        )),
    showlegend=False
)
tab2.plotly_chart(fig)