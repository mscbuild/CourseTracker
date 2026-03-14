import requests
from bs4 import BeautifulSoup

def search(query):
    url = f'https://www.coursera.org/search?query={query}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    courses = []
    for card in soup.select('.ais-InfiniteHits-item'):
        title_tag = card.select_one('h2')
        link_tag = card.select_one('a')
        if title_tag and link_tag:
            title = title_tag.text.strip()
            link = "https://www.coursera.org" + link_tag['href']
            courses.append({'title': title, 'url': link})
    return courses
