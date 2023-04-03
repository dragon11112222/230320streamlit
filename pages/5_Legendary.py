import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# reading dataset
df = pd.read_csv("pokemon5.csv", encoding='UTF-8')
df = df.drop(df[df.name == '야도킹'].index).reset_index(drop=True)
# print(len(df))

# sub_legendary, legendary, mythical 더미변수 합치기
category_list = []
for index, row in df.iterrows():
    if row.is_sub_legendary == 0:
        if row.is_legendary == 0:
            if row.is_mythical == 0:
                category_list.append('Normal')
            else:
                category_list.append('Mythical')
        else:
            category_list.append('Legendary')
    else:
        category_list.append('Sub_Legendary')
df['category'] = pd.DataFrame(category_list)
# print(df.category)

# legendary
st.header('sub_legendary & legendary & mythical')
fig = px.pie(df, names= 'category')
st.plotly_chart(fig)

# capture rate
st.header('Capture rate')
fig = px.histogram(df, x='catch_rate', color='category')
st.plotly_chart(fig)

# generation
st.header('Generation')
fig = px.histogram(df, x = 'generation', color='category')
st.plotly_chart(fig)

# type
st.header('Type')
fig = px.treemap(df, path=['type_1', 'category'])
st.plotly_chart(fig)

# # class
# st.header('Classification')
# fig = px.treemap(df, path=['classfication'])
# st.plotly_chart(fig)

# friendship
st.header('Friendship & Experience')
selection_list = ['Normal Pokemon', 'sub_legendary', 'legendary', 'mythical']
selected = st.selectbox('Category', selection_list)
if selected == 'Normal Pokemon':
    df_filtered = df[df.is_sub_legendary == 0]
    df_filtered = df_filtered[df_filtered.is_legendary == 0]
    df_filtered = df_filtered[df_filtered.is_mythical == 0]
else:
    df_filtered = df[df['is_%s' % selected] == 1]
fig = px.histogram(df_filtered, x = 'base_friendship', title='Friendship of %s' % selected)
st.plotly_chart(fig)
fig = px.histogram(df_filtered, x = 'base_experience', title='Experience of %s' % selected)
st.plotly_chart(fig)

# percentage_male
st.header('남녀비율')
fig = px.histogram(df, x='percentage_male', color='category')
st.plotly_chart(fig)