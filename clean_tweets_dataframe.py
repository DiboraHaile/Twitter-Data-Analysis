import pandas as pd


class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')

    def drop_duplicate(self)->pd.DataFrame:
        """
        drop duplicate rows
        """        
        return self.df.drop_duplicates()

    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        df['created_at'] = pd.to_datetime(self.df['created_at'])
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        df['polarity'] = pd.to_numeric(self.df['polarity'])
        df['subjectivity'] = pd.to_numeric(self.df['subjectivity'])
        df['retweet_count'] = pd.to_numeric(self.df['retweet_count'])
        df['favorite_count'] = pd.to_numeric(self.df['favorite_count'])
        
        return df

    def drop_null_col(self, df:pd.DataFrame)->pd.DataFrame:
        # removed columns containing null values of more than 20%
        row,col = df.shape
        df.dropna(axis='columns',thresh=row*0.8,inplace=True)
        print(df.columns)
        return df
        
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        df_new = df[df.lang == "en"]
        return df_new

    def special_chars(self,x):
        special_characters = '@_!#$%^&*()<>?/\|}{~:;[]'
        for char in special_characters:
            x = x.replace(char, '')
        x = x.encode('ascii', 'ignore').decode('ascii')
        return x

    def filter_text(self,df:pd.DataFrame) ->pd.DataFrame:
        df['original_text'] = self.df['original_text'].apply(lambda x: self.special_chars(x))
        # print(df['original_text'])
        return df