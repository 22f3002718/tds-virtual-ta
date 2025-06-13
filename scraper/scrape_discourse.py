import requests
import json
from bs4 import BeautifulSoup

def scrape_discourse(pages=2):
    base_url = "https://discourse.onlinedegree.iitm.ac.in"
    posts = []

    for page in range(1, pages+1):
        url = f"{base_url}/latest?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.select('.topic-title')
        for t in titles:
            title = t.get_text(strip=True)
            link = base_url + t.get('href')
            posts.append({'title': title, 'url': link})

    with open("data/discourse/discourse_posts.json", "w") as f:
        json.dump(posts, f, indent=2)

if __name__ == "__main__":
    scrape_discourse()
