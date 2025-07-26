from textblob import TextBlob
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
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
