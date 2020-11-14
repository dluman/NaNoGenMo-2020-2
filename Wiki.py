import bs4 as bs
import random
import requests
import wikipedia

class Entry:

    def __init__(self):
        self.title = None
        self.text = None
        self.cents = [
            i for i in range(-33,20) if i != 0
        ]
        self.get_entry()
    
    def suffix(self,cent):
        cent = str(
            abs(
                cent
            )
        )
        
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

    def adbc(self,cent):
        if cent < 0:
            return "BC"
        return ""
    
    def get_rulers(self):
        kings = []
        
        cent = random.choice(self.cents)
        cent_str = f"{self.suffix(cent)}-century_{self.adbc(cent)}"
        
        url = f"https://en.wikipedia.org/wiki/Category:{cent_str}_rulers"
        
        page = requests.get(url)
        pages = bs.BeautifulSoup(page.text,features="html.parser")
        
        refs = pages.find(id="mw-pages")
        
        links = refs.find_all('a')
        for link in links:
            href = link.get("href")
            if href.lower() not in ["list","wikipedia"]:
                kings.append(href)
        return kings
        
    def get_entry(self):
        kings = self.get_rulers()
        king = random.choice(kings)
        url = f"https://en.wikipedia.org/{king}"
        page = requests.get(url)
        soupy = bs.BeautifulSoup(page.text,features="html.parser")
        hdg = soupy.find(id="firstHeading").contents
        text = soupy.find(id="mw-content-text").get_text()
        
        self.title = hdg
        self.text = text