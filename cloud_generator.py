from collections import Counter
from wordcloud import WordCloud


def generate_wordcloud(text):
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate(text)
    return wordcloud


def extract_top_words(text, num_top_words=30):
    words = text.split()
    word_counts = Counter(words)
    top_words = word_counts.most_common(num_top_words)
    return top_words
