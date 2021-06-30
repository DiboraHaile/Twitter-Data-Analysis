import sqlite3
from sqlite3 import Error
import pandas as pd

def map_polarity(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'neutral'

def prepare_df(df):
    # cols_2_drop = ['source']
    # df = df.drop(columns=cols_2_drop, axis=1)
    df['polarity_name'] = df['polarity'].apply(lambda x: map_polarity(x))
    df['followers_count'] = pd.to_numeric(df['followers_count'])
    # df = df.fillna(0)
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
                                                 user_mentions)values(?,?,?,?,?,?,?,?,?,?,?)"""
        to_be_inserted = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],
                          row[10])

        cur.execute(insert_query,to_be_inserted)
        conn.commit() 
    cur.close()

def drop_table(table_name):
    conn, cur = connection_DB()
    drop_query = "DROP TABLE IF EXISTS "+table_name
    cur.execute(drop_query)
    conn.commit()
    cur.close()

def fetch_data(table_name):
    conn, cur = connection_DB()
    colmn_names = []
    select_query = "select * FROM "+table_name
    values =cur.execute(select_query)
    for desc in cur.description:
        colmn_names.append(desc[0])

    conn.commit()
    df = pd.DataFrame(values, columns=colmn_names)
    cur.close()
    return df

# def 

if __name__ == '__main__':
    create_table('twitter_data2')
    df = pd.read_csv('processed_tweet_data.csv')
    # df_new = prepare_df(df)
    # print(df)
    # print(df_new.columns)
    # drop_table('hello')
    # print(fetch_data('twitter_data'))    
    insert_data(df,'twitter_data2')