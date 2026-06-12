import pandas as pd
import re
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from wordcloud import WordCloud, STOPWORDS

nltk.download('vader_lexicon')
stopwords = set(STOPWORDS)

stopwords.update([
    'one',
    'will',
    'even',
    'much',
    'get',
    'make',
    'film',
    'movie',
    'show'
])


# Load the dataset
data = pd.read_csv("IMDB Dataset.csv")

# Display first 5 rows
print("First 5 Rows:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Display dataset shape
print("\nDataset Shape:")
print(data.shape)

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Display sentiment counts
print("\nSentiment Counts:")
print(data['sentiment'].value_counts())

# Clean review text

def clean_text(text):
    text = re.sub('<.*?>', '', text)      # Remove HTML tags
    text = re.sub('[^a-zA-Z ]', '', text) # Remove punctuation and numbers
    text = text.lower()                   # Convert to lowercase
    return text

# Create cleaned review column
data['clean_review'] = data['review'].apply(clean_text)

# Display cleaned reviews
print("\nCleaned Reviews:")
print(data[['review', 'clean_review']].head())

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Calculate sentiment scores
data['sentiment_score'] = data['clean_review'].apply(
    lambda x: sia.polarity_scores(x)['compound']
)

# Convert scores into labels
def vader_label(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

data['vader_sentiment'] = data['sentiment_score'].apply(vader_label)

# Display results
print("\nVADER Sentiment Counts:")
print(data['vader_sentiment'].value_counts())

print("\nSample Predictions:")
print(data[['sentiment', 'vader_sentiment']].head(10))

# Initialize VADER

import matplotlib.pyplot as plt

# Count VADER sentiments
sentiment_counts = data['vader_sentiment'].value_counts()

# Bar chart
plt.figure(figsize=(8,5))

bars = plt.bar(
    sentiment_counts.index,
    sentiment_counts.values,
    color=['green', 'red', 'gray']
)

# Add numbers above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(height),
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

plt.title("VADER Sentiment Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.show()

# Graph 2: VADER Sentiment Donut Chart

plt.figure(figsize=(8,8))

colors = ['green', 'red', 'gray']

plt.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.8
)

# Create donut hole
centre_circle = plt.Circle((0,0),0.55,fc='white')
plt.gca().add_artist(centre_circle)

plt.title(
    "VADER Sentiment Breakdown",
    fontsize=14,
    fontweight='bold'
)

plt.tight_layout()
plt.show()

# Graph 3: Positive Reviews Word Cloud

positive_text = " ".join(
    data[data['vader_sentiment'] == 'positive']['clean_review']
)

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color='white',
    colormap='Greens',
    stopwords=stopwords,
).generate(positive_text)

plt.figure(figsize=(12,6))

plt.imshow(wordcloud, interpolation='bilinear')

plt.axis("off")

plt.title(
    "Positive Review Word Cloud",
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout()
plt.show()

# Graph 4: Negative Reviews Word Cloud

negative_text = " ".join(
    data[data['vader_sentiment'] == 'negative']['clean_review']
)

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color='white',
    colormap='Reds',
    stopwords=stopwords,
).generate(negative_text)

plt.figure(figsize=(12,6))

plt.imshow(wordcloud, interpolation='bilinear')

plt.axis("off")

plt.title(
    "Negative Review Word Cloud",
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout()
plt.show()

# VADER Prediction Counts

print("\nVADER Prediction Counts:")
print(data['vader_sentiment'].value_counts())

# Compare actual vs VADER

comparison = pd.crosstab(
    data['sentiment'],
    data['vader_sentiment']
)

print("\nActual vs VADER:")
print(comparison)
correct = (data['sentiment'] == data['vader_sentiment']).sum()

total = len(data)

accuracy = round((correct / total) * 100, 2)

print(f"\nVADER Accuracy vs Actual Labels: {accuracy}%")