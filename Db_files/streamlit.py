import streamlit as st
import numpy as np
import pandas as pd
import query
import wordcloud
from wordcloud import WordCloud


def display_df():
    df = query.fetch_data('twitter_data')
    return df

# def search_bar():

def toggle_bn_pages():
    pages = ['Display Data Frame ','Visualize ']
    option = st.sidebar.selectbox('Choose:',pages)
    df = display_df()
    if option == pages[0]:
        st.markdown("<h1 style='color: gray;'>"+option+"of Twitter Data</h1>", unsafe_allow_html=True)
        st.write(df)

    else:
        st.markdown("<h1 style='color: gray;'>"+option+"Twitter Data</h1>", unsafe_allow_html=True)
        st.write('visualization here')
        text = ""
        for rows in df["original_text"]:
            text += rows
        wordcloud = WordCloud().generate(text)
        st.image(wordcloud.to_array())


toggle_bn_pages()
