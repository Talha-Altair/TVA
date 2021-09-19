import pandas as pd
import re
import string
import numpy as np
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


#remove URLs
def fix_URL(userImage):

   url = re.compile(r'https?://\S+|www\.\S+')

   return url.sub(r'', userImage)

#remove emojies
def remove_emojis(data):

   emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+", re.UNICODE)

   return re.sub(emoj, '', data)


#remove punctuations
def remove_punct(content):

   data = str.maketrans('','',string.punctuation)

   return content.translate(data)



def clean_text(text, words = None):

    stop_words = stopwords.words('english')

    words = [word for word in words if not word in stop_words]

    tokens = [word.lower() for word in word_tokenize(text)]

    return tokens


def start():

   pd.set_option('display.max_colwidth', None)

   #handle missing values of type NaN, N/a, na
   missing_value = ["NaN", "N/a", "na", np.nan]

   #import csv file
   df = pd.read_csv('static/user-feedback.csv', na_values = missing_value)

   df = df[["userName", "content", "score", "thumbsUpCount"]]

   #drop NaN values that have all rows empty
   data_dropped = df.dropna(how = "all")

   #heatmap
   #sns.heatmap(data.isnull(), yticklabels=False)

   #remove URLs
   # df['userImage'] = df['userImage'].apply(fix_URL)

   #remove emojies
   df['content'] = df['content'].apply(remove_emojis)

   #remove punctuations
   df['content'] = df['content'].apply(remove_punct)
   clean_text

   df['content'].dropna()

   df.to_csv("result.csv")




if __name__=='__main__':

    start()