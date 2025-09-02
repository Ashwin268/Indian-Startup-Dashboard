import pandas as pd
import streamlit as st

df = pd.read_csv('startup_funding.csv')

st.sidebar.title('Startup Funding Analysis Dashboard')
option = st.sidebar.selectbox('select one', ['Overall Analysis','StartUp', 'Investors'])
if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'StartUp':
    st.sidebar.selectbox('select StartUp',sorted(df['Startup Name'].unique()))
    btn1 = st.sidebar.button('Get StartUp Details')
    st.title('Startup Analysis')
else:
    st.sidebar.selectbox('select Investor',sorted(df['Investors Name'].fillna("Unknown").unique()))
    btn2= st.sidebar.button('Get Investor Details')
    st.title('Investors Analysis')