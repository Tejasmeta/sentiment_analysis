# app.py
import gradio as gr
import pickle

# Load model
with open('model/sentiment_model.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

def predict_sentiment(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return "😊 Positive" if prediction == 1 else "☹️ Negative"

# Gradio UI
interface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="Enter text here..."),
    outputs="text",
    title="Sentiment Analysis Tool",
    description="Predicts whether the sentiment of a sentence is Positive or Negative"
)

interface.launch()
