import streamlit as st
import numpy as np
import pandas as pd
import query
import wordcloud
from wordcloud import WordCloud


def display_df(table_name):
    df = query.fetch_data(table_name)
    return df

# def search_bar():

def toggle_bn_pages():
    pages = ['Display Data Frame ','Visualize ']
    data = ['Clean Data','Raw Data']
    option = st.sidebar.selectbox('Choose:',pages)
    display_data_option = st.sidebar.selectbox('Display:',data)
    if display_data_option == data[0]:
            df = display_df('twitter_data1')
    else:
        df = display_df('twitter_data')

    if option == pages[0]:
        st.markdown("<h1 style='color: gray;'>"+option+"of Twitter Data</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: gray;'>"+display_data_option+"</h2>", unsafe_allow_html=True)
        st.write(df)

    else:
        st.markdown("<h1 style='color: gray;'>"+option+"Twitter Data</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: gray;'>"+display_data_option+"</h2>", unsafe_allow_html=True)
        text = ""
        for rows in df["original_text"]:
            text += rows
        wordcloud = WordCloud().generate(text)
        st.image(wordcloud.to_array())


toggle_bn_pages()
