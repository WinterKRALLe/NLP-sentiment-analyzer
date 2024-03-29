import matplotlib.pyplot as plt
import numpy as np
from imdb_scraper import scrape_reviews
from analyzer import analyze_sentiment
from cloud_generator import generate_wordcloud, extract_top_words


def display_results(url):
    reviews = scrape_reviews(url)
    if not reviews:
        return

    print(url)

    sentiments = analyze_sentiment(reviews)
    all_text = ' '.join(reviews)
    wordcloud = generate_wordcloud(all_text)
    top_words = extract_top_words(all_text)

    plt.figure(figsize=(16, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    words, counts = zip(*top_words)
    plt.barh(range(len(words)), counts, color='skyblue')
    plt.yticks(range(len(words)), words)
    plt.gca().invert_yaxis()
    plt.title('Top 30 Words')
    plt.xlabel('Frequency')

    imdb_ratings = np.random.randint(1, 11, size=len(sentiments))

    plt.subplot(2, 1, 2)
    plt.scatter(sentiments, imdb_ratings, color='blue')
    plt.title('Sentiment vs. IMDb Ratings')
    plt.xlabel('Sentiment')
    plt.ylabel('IMDb Ratings')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def main():
    urls = [
        'https://www.imdb.com/title/tt15398776/reviews?ref_=tt_urv',
        'https://www.imdb.com/title/tt7286456/reviews?ref_=tt_urv',
        'https://www.imdb.com/title/tt0110912/reviews?ref_=tt_urv'
    ]

    for url in urls:
        display_results(url)


if __name__ == "__main__":
    main()
