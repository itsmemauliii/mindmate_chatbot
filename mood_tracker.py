import csv
from datetime import datetime

def save_entry(text, mood, sentiment):
    with open("data/entries.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), text, mood, sentiment])

def get_summary():
    moods = {"Positive": 0, "Negative": 0, "Neutral": 0}
    with open("data/entries.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            moods[row[2]] += 1
    return moods
