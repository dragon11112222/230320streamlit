import streamlit as st
import base64


# Set the URL or file path of the video
video_url = "https://youtu.be/mPaNK28VSoI"

# Use the media_player function to display the video
st.video(video_url)


st.header("주요 변수")


st.markdown('''
	* abilities: a stringified list of abilities that the pokémon is capable of having.
	* against_?: eighteen features that denote the amount of damage taken against an attack of a particular type of pokémon.
	* attack: the base attack of the pokémon.
	* base_egg_steps: the number of steps required to hatch an egg of the pokémon.
	* base_happiness: base happiness of the pokémon.
	* base_total: sum of hp, attack, defense, sp_attack, sp_defense and speed.
	* capture_rate: capture rate of the pokémon.
	* classification: the classification of the pokémon as described by the Sun and Moon pokédex.
	* defense: the base defense of the pokémon.
	* experience_growth: the experience growth of the pokémon.
	* height_m: height of the pokémon in metres.
	* hp: the base HP of the pokemon. It is short for Hit Point, which determines how much damage a pokémon can receive before fainting.
	* japanese_name: the original Japanese name of the pokémon.
	* name: the English name of the pokémon.
	* percentage_male: the percentage of the species that are male. Blank if the pokémon is genderless.
	* pokedex_number: the entry number of the pokémon in the National Pokédex.
	* sp_attack: the base special attack of the pokémon.
	* sp_defense: the base special defense of the pokémon.
	* speed: the base speed of the pokémon.
	* type1: the primary type of the pokémon.
	* type2: the secondary type of the pokémon.
	* weight_kg: the weight of the pokémon in kilograms.
	* generation: the numbered generation which the pokémon was first introduced.
	* is_legendary: denotes if the pokémon is legendary.
''')
import streamlit as st
import pandas as pd
