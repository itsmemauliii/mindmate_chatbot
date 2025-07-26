from textblob import TextBlob
import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_message(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    mood = "Neutral"
    if sentiment > 0.3:
        mood = "Positive"
    elif sentiment < -0.3:
        mood = "Negative"

    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return mood, entities, sentiment
