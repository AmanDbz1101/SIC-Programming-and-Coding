import streamlit as st 

import pandas as pd 

st.header("This is it")

df = pd.read_csv("spotify_songs_2025.csv")

names = df['Artist'].unique()
