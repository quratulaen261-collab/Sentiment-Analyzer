import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Streamlit UI
st.title("Text_Sentiment Analyzer")

text = st.text_input("Enter text:", value="I love learning Python!")

if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        scores = sia.polarity_scores(text)
        compound = scores['compound']

        # Determine sentiment
        if compound >= 0.05:
            sentiment = "positive"
        elif compound <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        st.success("Analysis complete!")
        st.write(f"**Sentiment:** `{sentiment}`")




