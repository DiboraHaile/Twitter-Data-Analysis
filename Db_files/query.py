import sqlite3
from sqlite3 import Error
import pandas as pd

def prepare_df(df):
    cols_2_drop = ['source', 'place', 'possibly_sensitive']
    df = df.drop(columns=cols_2_drop, axis=1)
    df = df.fillna(0)
    return df


def connection_DB():
    conn = sqlite3.connect("twitter_db.db")
    cur = conn.cursor()
    return conn,cur

def create_table(table_name):
       
    create_query = " CREATE TABLE IF NOT EXISTS "+table_name+""" (id INTEGER PRIMARY KEY NOT NULL,
    created_at TEXT NOT NULL,
    original_text TEXT DEFAULT NULL,
    polarity FLOAT DEFAULT NULL,
    subjectivity FLOAT DEFAULT NULL, 
    language TEXT DEFAULT NULL,
    favorite_count INT DEFAULT NULL,
    retweet_count INT DEFAULT NULL,
    original_author TEXT DEFAULT NULL,
    followers_count INT DEFAULT NULL,
    friends_count INT DEFAULT NULL,
    hashtags TEXT DEFAULT NULL,
    user_mentions TEXT DEFAULT NULL)""" 
    conn, cur = connection_DB()
    cur.execute(create_query)
    conn.commit() 
    cur.close()

def insert_data(df: pd.DataFrame,table_name):
    conn, cur = connection_DB()
    for _,row in df.iterrows():
        print(len(row))
        insert_query = "INSERT INTO "+ table_name + """(created_at,
                                                original_text, polarity, subjectivity,                                             
                                                language,favorite_count,retweet_count,
                                                original_author, followers_count,friends_count,
                                                hashtags, user_mentions)values(?,?,?,?,?,?,?,?,?,?,?,?)"""
        to_be_inserted = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],
                          row[10],row[11])

        cur.execute(insert_query,to_be_inserted)
        conn.commit() 
    cur.close()

# def fetch_al

def fetch_data(table_name):
    conn, cur = connection_DB()
    colmn_names = []
    for desc in cur.description:
        colmn_names.append(desc[0])
    df = pd.DataFrame(cur.fetchall(), columns=colmn_names)
    return df

if __name__ == '__main__':
    create_table('twitter_data')
    df = pd.read_csv('processed_tweet_data.csv')
    df_new = prepare_df(df)
    print(df_new.columns)
    insert_data(df_new,'twitter_data')