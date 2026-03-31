import pandas as pd
import streamlit as st
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSaaJ9rWNUjHOSg_THtpEkN1nsvpgBcNz0s_sweLewE5QYvF2ZBWHQ2bO5ixvCKBfwsfyXP7HATxIXV/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)
st.title("Monitoramento IoT")
st.line_chart(df[['temperatura', 'umidade']])
st.dataframe(df)
