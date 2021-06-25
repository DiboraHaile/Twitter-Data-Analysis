import streamlit as st
import numpy as np
import pandas as pd
import query

pages = ['Display Data Frame ','Visualize ']
def display_df():
    df = query.fetch_data('twitter_data')
    return df

def toggle_bn_pages():
    option = st.sidebar.selectbox('Choose:',pages)
    return option

page = toggle_bn_pages()
if page == pages[0]:
    st.markdown("<h1 style='color: gray;'>"+page+"of Twitter Data</h1>", unsafe_allow_html=True)
    df = display_df()
    st.write(df)

else:
    st.markdown("<h1 style='color: gray;'>"+page+"Twitter Data</h1>", unsafe_allow_html=True)
    st.write('visualization here')