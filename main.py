from Wiki import Entry
from King import Bio
from Vader import Sentiment

entry = Entry()

#print(f"{entry.title} {entry.text}")

king = Bio(entry.title, entry.text)

print(Sentiment.classify(entry.text))
