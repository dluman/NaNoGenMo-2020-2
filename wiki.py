import bs4 as bs
import random
import requests
import wikipedia

from nltk.sentiment.vader import SentimentIntensityAnalyzer as sentimentalizer

VADER = sentimentalizer()

INTROS = [
    "Now let me tell you about",
    "Of course, there's",
    "I recall",
    "I've heard about",
    "There's this one --",
    "Years ago, I read about",
    "As those of you up on your history know, there's",
    "How about that",
    "Who could forget",
    "I'd be remiss if I forgot",
    "I'd like to address the legacy of",
    "If we're thinking of kings, let's include",
]

MEAN_SUFFIXES = [
    "That was one mean king.",
    "Oh, talk about mean kings.",
    "If you're looking for a definition of a mean king, look no further.",
    "Were they ever mean!",
    "Meanness was one of their main qualities.",
    "\"Mean\" doesn't begin to cover it.",
    "Not a nice bone in their body.",
    "They redefined mean."
]

NOT_SO_MEAN_SUFFIXES = [

]

NEUTRAL_SUFFIXES = [
]

KIND_SUFFIXES = [
]

NICE_SUFFIXES = [
]

KINGS_IVE_KNOWN = [
]

def suffix(cent):
    cent = str(abs(cent))
    if int(cent) in range(10,19):
        cent += "th"
    elif cent[-1] == "1":
        cent+= "st"
    elif cent[-1] == "2":
        cent += "nd"
    elif cent[-1] == "3":
        cent += "rd"
    else:
        cent += "th"
    return cent

def adbc(cent):
    if cent < 0:
        return "BC"
    return ""

def write_entry(name,text):
    intro = random.choice(INTROS)
    assessment = assess(text)
    event = tokenize(text)
    print(f"{intro} {name[0]}. {assessment} {random.choice(event)}.")

def assess(text):
    assessment = None
    sentiment = sentimentalize(text)
    cmp = sentiment["compound"]
    if cmp < -.5:
        assessment = random.choice(MEAN_SUFFIXES)
    return assessment

def tokenize(text):
    text = text.split(".")
    return text

def sentimentalize(text):
    return VADER.polarity_scores(text)

cents = [i for i in range(-33,20) if i != 0]

for i in range(20):
    kings = []
    cent = random.choice(cents)
    cent_str = f"{suffix(cent)}-century_{adbc(cent)}"
    url = f"https://en.wikipedia.org/wiki/Category:{cent_str}_rulers"
    page = requests.get(url)
    pages = bs.BeautifulSoup(page.text,features="html.parser")
    refs = pages.find(id="mw-pages")
    links = refs.find_all('a')
    for link in links:
        href = link.get("href")
        if not "list" in href.lower() and not "wikipedia" in href:
            kings.append(href)
    #print(kings)
    vader = sentimentalizer()

    for king in kings:
        if king not in KINGS_IVE_KNOWN:
            url = f"https://en.wikipedia.org/{king}"
            page = requests.get(url)
            soupy = bs.BeautifulSoup(page.text,features="html.parser")
            hdg = soupy.find(id="firstHeading").contents
            text = soupy.get_text()
            #print(sentimentalize(text))
            write_entry(hdg,text)
            KINGS_IVE_KNOWN.append(king)
