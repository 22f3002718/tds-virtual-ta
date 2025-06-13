import requests
from bs4 import BeautifulSoup

def scrape_course():
    url = "https://example-course-url"  # Replace with actual course page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content = soup.get_text()

    with open("data/course/course.txt", "w") as f:
        f.write(content)

if __name__ == "__main__":
    scrape_course()
