import bs4 as bs
import random
import requests
import wikipedia

from nltk.sentiment.vader import SentimentIntensityAnalyzer as sentimentalizer

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

cents = [i for i in range(-33,20) if i != 0]

for i in range(1):
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
    print(kings)
    vader = sentimentalizer()

    for king in kings:
        url = f"https://en.wikipedia.org/{king}"
        page = requests.get(url)
        soupy = bs.BeautifulSoup(page.text,features="html.parser")
        text = soupy.get_text()
        print(f"{king} {vader.polarity_scores(text)}")
