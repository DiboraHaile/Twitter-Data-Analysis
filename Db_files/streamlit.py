import streamlit as st
import numpy as np
import pandas as pd
import query


st.markdown("<h1 style='color: gray;'>Twitter Data</h1>", unsafe_allow_html=True)
df = query.fetch_data('twitter_data')
# st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
st.write(df)