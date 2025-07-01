# train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
df = pd.read_csv('Tweets.csv')

# Filter necessary columns
df = df[['text', 'airline_sentiment']]
df = df[df['airline_sentiment'] != 'neutral']  # Keep only positive/negative
df['label'] = df['airline_sentiment'].apply(lambda x: 1 if x == 'positive' else 0)

# Features and labels
X = df['text']
y = df['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model and vectorizer
with open('model/sentiment_model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)
