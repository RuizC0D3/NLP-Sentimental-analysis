 # -*- coding: utf-8 -*-
"""
D4V1D TEST
"""

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#Dodnload NLTK
nltk.download('vader_lexicon')

#Start analyzer of sentiments
sia = SentimentIntensityAnalyzer()

def load_comments(file_path):
    """Upload comments and use only valid comments"""
    df = pd.read_csv(file_path)
    return df.dropna(subset=['Comment'])

def analyze_sentiment(df):
    """apply the analyzer of sentimens"""
    df['sentiment_score'] = df['Comment'].apply(lambda comment: sia.polarity_scores(comment)['compound'])
    return df

def calculate_average_sentiment(df, max_comments=200):
    """Get the average value of 'max_comments' comments."""
    num_comments = min(max_comments, len(df))
    return df['sentiment_score'][:num_comments].mean(), num_comments

def main():
    file_path = 'comments.csv'  # route of CSV
    df = load_comments(file_path)
    df = analyze_sentiment(df)
    
    avg_sentiment, num_comments = calculate_average_sentiment(df)
    
    # Show results
    print(f'Promedio de sentimiento de los primeros {num_comments} comentarios: {avg_sentiment:.4f}')
    
    #Interpretación de los resultados
    if (avg_sentiment > 0):
        print("Lo que quiere decir que son sentimientos positivos")
    elif (avg_sentiment == 0):
        print("Lo que quiere decir que son sentimiento neutros")
    else:
         print("Lo que quiere decir que son sentimiento negativos")

if __name__ == "__main__":
    main()