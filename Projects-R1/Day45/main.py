from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

movies = response.text

soup = BeautifulSoup(movies, 'html.parser')

movies = soup.find_all(class_="article-title-description__text")

movies_titles = [title.find("h3").getText() for title in movies][::-1]

df = pd.DataFrame(movies_titles)

df.to_csv('top100_movies', index=False, header=False)
