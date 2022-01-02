import yfinance as yf
import streamlit as st
import datetime
import pandas as pd
import requests
yf.pdr_override()

st.write("""
# The Data Incubator 12-day milestone project
""")

st.sidebar.header('User Input Parameters')

today = datetime.date.today()
def user_input_features():
    ticker = st.sidebar.text_input("Ticker", 'MSFT')
    start_date = st.sidebar.text_input("Start Date", '2021-01-01')
    end_date = st.sidebar.text_input("End Date", f'{today}')
    return ticker, start_date, end_date

symbol, start, end = user_input_features()

start = pd.to_datetime(start)
end = pd.to_datetime(end)

# Read data
data = yf.download(symbol,start,end)

st.header(f"Adjusted Close Price")
st.line_chart(data['Adj Close'])