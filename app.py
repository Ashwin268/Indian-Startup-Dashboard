import pandas as pd
import streamlit as st

df = pd.read_csv('startup_funding.csv')

df['Investor Name'] = df['Investor Name'].fillna('Unknown')

st.sidebar.title('Startup Funding Analysis Dashboard')
option = st.sidebar.selectbox('select one')