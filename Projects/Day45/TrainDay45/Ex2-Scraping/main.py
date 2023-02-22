from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")

yc_combinator = response.text

soup = BeautifulSoup(yc_combinator, 'html.parser')

articles = soup.find_all(class_="titleline")
print(articles)
print("-------------------------------------------------")
article_texts = [text.find(name="a").getText() for text in articles]
article_links = [link.find(name="a").get("href") for link in articles]
article_up_votes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_up_votes)


index_max = article_up_votes.index(max(article_up_votes))

print(article_texts[index_max])
print(article_links[index_max])
