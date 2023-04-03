import plotly
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
sns.set_style("whitegrid")
import squarify

import streamlit as st

import plotly.io as pio
pio.templates.default = "plotly"


import matplotlib.font_manager as fm
font = fm.FontProperties('NanumGothic.ttf')

from matplotlib import rc
rc('font',family = 'AppleGothic')
plt.rcParams['axes.unicode_minus'] =False

st.title("포켓몬의 여러가지 파라미터에 대해 알아보자....")

data = pokemon = df = pd.read_csv("pokemon5.csv", encoding = "UTF-8")
df = df.drop(df[df.name == '야도킹'].index).reset_index(drop=True)

fig1 = plt.figure(figsize=(12,6))
ax = sns.countplot(x='generation',data=df,order=df['generation'].value_counts().index)
ax.set_title('Pokemons per Generation')
ax.set(xlabel='Generation',ylabel='Count')
st.pyplot(fig1)


poke_df = df




# Group the dataset by generation and legendary status and count the number of pokemons in each group
legendary_counts = poke_df.groupby(['generation', 'is_legendary']).size().reset_index(name='Count')

# Filter the dataset to only include legendary pokemons
legendary_counts = legendary_counts[legendary_counts['is_legendary'] == 1]

# Visualize the number of legendary pokemons per generation using a bar chart
fig = px.bar(legendary_counts, x='generation', y='Count', text='Count', title='Number of Legendary Pokemons per Generation')
fig.update_traces(textposition='auto', textfont_size=20)
st.plotly_chart(fig, use_container_width=True)




valc_type1 = df['type_1'].value_counts()

fig2 = plt.figure(figsize=(20,10))
ax = squarify.plot(valc_type1,
                  label = valc_type1.index,
                  color = sns.color_palette('husl',len(valc_type1)),
                  pad=0.8,
                  text_kwargs={'fontsize':20})
ax.set_title("타입별 비율", size=20)
plt.axis('off')
st.pyplot(fig2)




##################
# valc_type2 = df['type_2'].value_counts()
# types_df = pd.concat([valc_type1,valc_type2],axis=1)

# fig3 = types_df.plot(kind='bar',stacked=True, color=['red', 'green'],figsize=(12,6))
# st.pyplot(fig3)


########################################

df = df[df['is_legendary'] == True]

# group data by generation and calculate mean capture rate
df_grouped = df.groupby('generation')['catch_rate'].mean().reset_index()

# create the plot
fig4 = px.bar(df_grouped, x='generation', y='catch_rate', 
             color='generation', 
             labels={'generation': 'Generation', 'catch_rate': 'Mean Capture Rate'},
             title='Generation wise Capture Rate amongst Legendary Pokemons')

# update layout
fig4.update_layout(title_x=0.5, 
                  xaxis_tickfont_size=14,
                  yaxis=dict(title_font_size=16),
                  legend=dict(title_font_size=16))


st.plotly_chart(fig4, use_container_width=True)

#FIG5################################################################
fig5 = plt.figure(figsize=(20,6))
ax = sns.countplot(data=df, x="abilities_number", hue="is_legendary")
# ax.set_title("포켓몬 능력 수",fontproperties=font, size=20)
ax.set(xlabel="Number of Abilities", ylabel="Count");
ax.legend(["Non-legendary", "Legendary"], loc='upper right');
st.pyplot(fig5)

#FIG6##################################################################
fig6 = plt.figure(figsize=(10,6))
ax = sns.scatterplot(x='weight_kg', y='height_m', data=df, hue='is_legendary', palette=['red'])
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, ["Non-legendary", "Legendary"])


top5_weight_height_merged = pd.concat([df.nlargest(5, 'height_m'), df.nlargest(5, 'weight_kg')]).drop_duplicates(subset=['name'])
for index, row in top5_weight_height_merged.iterrows():
    plt.annotate(row['name'], xy=(row['weight_kg'], row['height_m']), fontsize=10)
st.pyplot(fig6)

#FIG7####################################################################

# grid_kws = {"height_ratios": (.9, .05), "hspace": .25}
# f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws, figsize=(20,10))
# fig7 = sns.heatmap((df[df['is_legendary']==0][['hp','sp_attack','sp_defense','attack','defense','speed']]).corr(),
#            annot=True,
#            fmt=".2f",
#            ax=ax,
#            cbar_ax=cbar_ax,
#            cmap='tab20c')
# st.pyplot(fig7)

# #FIG8######################################################################
# grid_kws = {"height_ratios": (.9, .05), "hspace": .25}
# f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws, figsize=(20,10))
# sns.heatmap((df[df['is_legendary']==1][['hp','sp_attack','sp_defense','attack','defense','speed']]).corr(),
#            annot=True,
#            fmt=".2f",
#            ax=ax,
#            cbar_ax=cbar_ax,
#            cmap='tab20c')

#FIG9#######################################################################

fig9,axes = plt.subplots(2,2,figsize=(16,10),sharey=True)
sns.scatterplot(x= data['attack'],y =data['speed'],ax=axes[0,0])
axes[0,0].set_title("Speed V/S Attack")
sns.scatterplot(x= data['defense'],y= data['speed'],ax=axes[0,1])
axes[0,1].set_title("Speed V/S Defence")
sns.scatterplot(x= data['height_m'],y= data['speed'],ax=axes[1,0])
axes[1,0].set_title("Speed V/S Height")
sns.scatterplot(x= data['weight_kg'],y= data['speed'],ax=axes[1,1])
axes[1,1].set_title("Speed V/S Weight")
#fig9.set_title("Speed Factor?", size=20)

st.pyplot(fig9)

#FIG10##########################################################################

# non_legendary_pokemon_attributes = df[df["is_legendary"]==0].groupby(['type_1']).median()[["attack", "sp_attack", "defense", "sp_defense", "hp", "speed", "total_points"]]


# # Filter for non-legendary Pokémon only
# df_non_legendary = df[df['is_legendary'] == 0]

# # Calculate the median of attributes by type
# df_medians = df_non_legendary.groupby('type_1').median().reset_index()

# # Melt the dataset to create a long-form dataframe
# df_melt = pd.melt(df_medians, id_vars=['type_1'], value_vars=['attack', 'defense', 'sp_attack', 'sp_defense', 'speed'])

# # Plot the box plot
# fig10 = fig = px.box(df_melt, x='type_1', y='value', color='variable',
#              title='Median of Attributes by Type of Non-legendary Pokémon')

# st.plotly_chart(fig10, use_container_width=True)
#FIG11#########################################################################

df_legendary = df[df["is_legendary"] == 1]

# Create the scatter plot
fig11 = px.scatter(df_legendary, x="total_points", y="name", color="type_1", size="height_m", hover_name="name", hover_data=["total_points", "generation"])


# Set the title and axis labels
fig11.update_layout(title="Legendary Pokemon with their Total Points",
                  xaxis_title="Total Points",
                  yaxis_title="Pokemon Name")

# Change the color scale
fig11.update_traces(marker=dict(colorscale="Viridis"))

# Change the size range
fig11.update_traces(marker=dict(sizemode='diameter', size=20))

# Change the hover label format
fig11.update_traces(hovertemplate="<b>%{hovertext}</b><br><br>Type: %{marker.color}<br>Height: %{marker.size:.1f} m<br>Total Points: %{customdata[0]}<br>Generation: %{customdata[1]}")

# Show the plot
st.plotly_chart(fig11, use_container_width=True)

#FIG12####################################################################




#FIG13#####################################################

top10_pokemon_base_total = df.sort_values(by="total_points", ascending=False).reset_index()[:10]

fig13 = plt.figure(figsize=(20,10))
ax = sns.barplot(y=top10_pokemon_base_total["name"], x=top10_pokemon_base_total["total_points"], orient='h')
ax.set_title("Which is the best pokemon?", size=20)
ax.set(xlabel="Total Points", ylabel="Name")

# Annotate value labels to each pokémon
for index, row in top10_pokemon_base_total.iterrows(): 
    plt.annotate(row["total_points"], xy=(row["total_points"]-20, index), color='white') 

st.pyplot(fig13)


#FIG14###################################################




pokemon_attack = pokemon.groupby('name')['attack'].sum().reset_index().sort_values('attack',ascending =False)
fig14 = px.bar(pokemon_attack[:50], y='attack', x='name', color='attack', height=600)
fig14.update_layout(
    title='Top 50 Attacking Pokemons')

st.plotly_chart(fig14, use_container_width=True)
#FIG15###################################################


#FIG16###################################################

pokemon[['ability_2','ability_hidden']] = pokemon[['ability_2','ability_hidden']].fillna(value='NO INFO')
pokemon_ablity = pokemon.groupby(['name','abilities_number'])['ability_1','ability_2','ability_hidden'].sum().reset_index().sort_values('name',ascending =False)
pokemon_ablity

fig16 = px.scatter_3d(pokemon_ablity, x="ability_1", y="ability_2", z="ability_hidden", color="abilities_number", size="abilities_number", hover_name="name",
                  symbol="abilities_number")
fig16.update_layout(coloraxis_colorbar=dict(
    title="Ability of Pokemon",
    tickvals=[1,2,3],
    ticktext=["ability_1","ability_2","ability_hidden"],
    lenmode="pixels", len=150,
))
fig16.update_layout(
    title='캐릭터별 능력 비교')


st.plotly_chart(fig16, use_container_width=True)


#FIG17####################################################



fig17 = px.scatter_3d(df, x='attack', y='defense', z='hp', color='type_1', symbol='type_2', hover_name='name')

fig17.update_layout(scene=dict(xaxis_title='attack', yaxis_title='defense', zaxis_title='hp'),
                  legend=dict(title='type_1'))


st.plotly_chart(fig17, use_container_width=True)


#FIG18##############################################


#FIG19#############################################


#FIG20###########################################

against_df = df.filter(regex='against')

# Rename the columns to remove the "against_" prefix
against_df = against_df.rename(columns=lambda x: x.replace('against_', ''))

# Create a heatmap of the against variables data
fig20 = plt.figure(figsize=(10, 8))
sns.heatmap(against_df, cmap='coolwarm', annot=True, fmt='.1f')
plt.title('Against Variables Heatmap')


st.pyplot(fig20)
#############################################



# Load Pokemon data
poke_df = pd.read_csv("pokemon5.csv")

# Allow user to select multiple Pokemon
selected_pokemon = st.multiselect("Select your Pokemon", poke_df["name"])

# Allow user to select the variable to use for the calculation
calculation_var = st.selectbox("Select the variable to use for calculation", 
                               ["total_points", "hp", "attack", "defense", 
                                "sp_attack", "sp_defense", "speed", 
                                "catch_rate", "base_friendship", "base_experience", 
                                "against_bug", "against_dark", "against_dragon", 
                                "against_electric", "against_fairy", "against_fight", 
                                "against_fire", "against_flying", "against_ghost", 
                                "against_grass", "against_ground", "against_ice", 
                                "against_normal", "against_poison", "against_psychic", 
                                "against_rock", "against_steel", "against_water"])

# Filter the DataFrame to only include selected Pokemon
filtered_poke_df = poke_df[poke_df["name"].isin(selected_pokemon)]

# Get Pokemon with highest or lowest base total, depending on calculation_var
if not filtered_poke_df.empty:
    if calculation_var.startswith("against_"):
        best_poke = filtered_poke_df.loc[filtered_poke_df[calculation_var].idxmin()]
    else:
        best_poke = filtered_poke_df.loc[filtered_poke_df[calculation_var].idxmax()]

    # Display the best Pokemon
    st.write("Best Pokemon: ")
    st.write(best_poke["name"])
    st.write("Type 1: ", best_poke["type_1"])
    st.write("Type 2: ", best_poke["type_2"])
    st.write(f"{calculation_var.replace('_', ' ').title()}: ", best_poke[calculation_var])
else:
    st.write("No Pokemon selected.")



