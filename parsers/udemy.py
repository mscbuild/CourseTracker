import requests
from bs4 import BeautifulSoup

def search(query):
    url = f'https://www.udemy.com/courses/search/?q={query}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    courses = []
    for card in soup.select('.course-card--main-content--3xEIw'):
        title_tag = card.select_one('.udlite-focus-visible-target.udlite-heading-md.course-card--course-title--2f7tE')
        link_tag = card.select_one('a')
        if title_tag and link_tag:
            title = title_tag.text.strip()
            link = "https://www.udemy.com" + link_tag['href']
            courses.append({'title': title, 'url': link})
    return courses
