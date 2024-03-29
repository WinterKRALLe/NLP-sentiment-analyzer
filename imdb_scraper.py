import requests
from bs4 import BeautifulSoup


def scrape_reviews(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        review_divs = soup.find_all(
            'div',
            class_='lister-item mode-detail imdb-user-review collapsable'
        )
        reviews = [
            review_div.find(class_='text').get_text(strip=True)
            for review_div in review_divs
        ]
        return reviews
    except Exception as e:
        print(f"Error scraping reviews from {url}: {e}")
        return []
