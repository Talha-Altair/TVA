import pandas as pd
import re
import string
import numpy as np
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def fix_URL(userImage):

	url = re.compile(r'https?://\S+|www\.\S+')

	return url.sub(r'', userImage)

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

def clean_text(row):

	content = row['content']

	all_words = content.split()

	stop_words = stopwords.words('english')

	raw_words_list = [word for word in all_words if not word in stop_words]

	raw_words = ' '.join(raw_words_list)

	row['raw_words'] = raw_words

	print(row['raw_words'])

	return row

def prepocess():

	pd.set_option('display.max_colwidth', None)

	missing_value = ["NaN", "N/a", "na", np.nan]

	df = pd.read_csv('static/user-feedback.csv', na_values = missing_value)

	df = df[["userName", "content", "score", "thumbsUpCount"]]

	data_dropped = df.dropna(how = "all")

	df['content'] = df['content'].apply(remove_emojis)

	#remove punctuations
	df['content'] = df['content'].apply(remove_punct)

	df = df.apply(clean_text, axis=1)

	df = df.dropna()

	return df

def sentiment_scores(row):
    
    sentence = row["content"]
 
    sid_obj = SentimentIntensityAnalyzer()
 
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    row["polarity_score"] = sentiment_dict['compound']
    
    return row

def assign_cols(df):

	df = df.apply(sentiment_scores, axis = 1)

	return df

def startpy():

	df = prepocess()

	df = assign_cols(df)


if __name__=='__main__':

	startpy()
