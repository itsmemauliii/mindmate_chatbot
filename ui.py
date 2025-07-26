import streamlit as st
from chat import analyze_message
from mood_tracker import save_entry, get_summary

st.title("🧘 MindMate – Your Reflection Buddy")

text_input = st.text_area("What's on your mind today?")

if st.button("Reflect"):
    mood, entities, sentiment = analyze_message(text_input)
    save_entry(text_input, mood, sentiment)
    
    st.write(f"🧠 Detected Mood: **{mood}**")
    st.write(f"📌 Key Mentions: {entities}")

if st.button("Show Weekly Mood Summary"):
    summary = get_summary()
    st.write(summary)
