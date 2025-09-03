import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('startup_cleaned.csv')

def loadInvestorDetails(Investor):
    st.title(Investor)

    #loading most recent investments
    most_recent_investments = df[df['Investor'].str.contains(Investor)].head(5)[['Date', 'Startup Name', 'Vertical', 'City', 'Round', 'Amount in Cr']]
    st.subheader('Most recent Investments')
    st.dataframe(most_recent_investments)

    col1, col2 = st.columns(2)
    with col1:
        #loading biggest Investment
        big_inv = df[df['Investor'].str.contains(Investor)].groupby('Startup Name')['Amount in Cr'].sum().sort_values(ascending=False).head(5)
        st.subheader('Top 5 Biggest Investments')
        fig, ax = plt.subplots()
        big_inv.plot(kind='bar', ax=ax, color='cyan')
        ax.set_xlabel('Startup Name')
        ax.set_ylabel('Amount in Cr')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

    # with col2:

st.sidebar.title('Startup Funding Analysis Dashboard')
option = st.sidebar.selectbox('select one', ['Overall Analysis','StartUp', 'Investors'])
if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'StartUp':
    st.sidebar.selectbox('select StartUp',sorted(df['Startup Name'].unique()))
    btn1 = st.sidebar.button('Get StartUp Details')
    st.title('Startup Analysis')
else:
    selectedInvestor = st.sidebar.selectbox('select Investor',sorted(set(df['Investor'].str.split(',').sum())))
    btn2= st.sidebar.button('Get Investor Details')
    if btn2:
        loadInvestorDetails(selectedInvestor)