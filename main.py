from Wiki import Entry
from King import Bio
from Vader import Sentiment

with open('mean_kings.txt','w') as o:
    for i in range(200):
        entry = Entry()
        king = Bio(entry.title, entry.text)
        o.write(king.entry + "\n\n")
        o.write("--------\n\n")
