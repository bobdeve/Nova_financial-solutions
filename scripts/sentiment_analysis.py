# sentiment_analysis.py
from textblob import TextBlob
import pandas as pd

def calculate_sentiment(text):
    """Calculate sentiment polarity using TextBlob."""
    return TextBlob(text).sentiment.polarity

def apply_sentiment(df, text_column='headline'):
    """Apply sentiment analysis to a given column of a DataFrame."""
    df['Sentiment'] = df[text_column].apply(calculate_sentiment)
    return df
