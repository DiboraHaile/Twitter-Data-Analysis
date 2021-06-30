from os import write
import streamlit as st
import numpy as np
import pandas as pd
import query
import wordcloud
import plotly.express as px
import numpy as np
from wordcloud import WordCloud


def display_df(table_name):
    df = query.fetch_data(table_name)
    df_prepared = query.prepare_df(df)
    return df_prepared

def select_data_df(table_name):
    df = query.select_data(table_name)
    return df

def input_text():
    name = st.text_input("Choose the")
    if(st.button('Submit')):
        result = name.title()
        st.success(result)

def plotbar_graph(df,title,header):
    st.subheader(header)
    st.write(title)
    st.bar_chart(df)

# def select_tweets():


def select_attributes_Df():
    df = display_df('twitter_data1')
    display_options = st.selectbox("Choose the information to be displayed: ",
                     ['Popular Authors', 'Tweet polarity count', 'All data']) 
    if display_options == 'Popular Authors':
        df_authors = df.sort_values(by=['followers_count'],ascending=False)
        popular_authors = df_authors[df_authors.followers_count > 10000]
        st.write(popular_authors[['original_author','original_text','followers_count','friends_count']])
    elif display_options == 'Tweet polarity count':
        st.write(df.groupby('polarity_name').count()['polarity'])
    else:
        st.write(df) 

def select_tweets():
    df = display_df('twitter_data1')
    st.markdown("<h2 style='color: gray;background-color:rgb(0, 20, 34);'> Select information of an author</h2>", unsafe_allow_html=True)
    author_name = st.selectbox("Author's name: ",df['original_author'])
    st.write(df[df['original_author'] == author_name])

def toggle_bn_pages():
    pages = ['Display Data Information ','Visualize ']
    option = st.sidebar.selectbox('Choose:',pages)
    df = display_df('twitter_data1')
    if option == pages[0]:
        st.markdown("<h1 style='color: gray;'>"+option+"of Twitter Data</h1>", unsafe_allow_html=True)
        select_attributes_Df()
        select_tweets()

    else:
        st.markdown("<h1 style='color: gray;'>"+option+"Twitter Data</h1>", unsafe_allow_html=True)
        text = ""
        for rows in df["original_text"]:
            text += rows
        st.markdown("<h2 style='color: gray;background-color:rgb(0, 20, 34);'>Display wordcloud</h2>", unsafe_allow_html=True)
        wordcloud = WordCloud().generate(text)
        st.image(wordcloud.to_array())
        if st.checkbox("Show charts"):
        
            df_authors = pd.DataFrame({'popular authors':df.groupby(['original_author'])['followers_count'].max()}).reset_index()
            df_authors = df_authors.sort_values(['popular authors'],ascending=False)
            level = st.slider("Select", 1, 20)
            if level == 1:
                st.markdown("<h2 style='color: gray;background-color:rgb(0, 20, 34);'>Barchart of the most popular author based on follower count</h2>", unsafe_allow_html=True)
            else:
                st.markdown("<h2 style='color: gray;background-color:rgb(0, 20, 34);'>Barchart of top "+str(level)+" authors based on follower count</h2>", unsafe_allow_html=True)
            col1, col2 = st.beta_columns([4,2])
            with col1:
                plotbar_graph(df_authors.head(level),'','')
            with col2:    
                st.write(df_authors['original_author'].head(level))

            df_polarity = pd.DataFrame({'polarity_count':df.groupby(['polarity_name'])['original_text'].count()}).reset_index()
            st.markdown("<h2 style='color: gray;background-color:rgb(0, 20, 34);'>PieChart of Polarity count</h2>", unsafe_allow_html=True)
            fig = px.pie(df_polarity, values='polarity_count',names='polarity_name', title='')
            st.plotly_chart(fig)
            # fig.show()
        



toggle_bn_pages()

# input_text()