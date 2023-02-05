import os
from datetime import date, timedelta
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TODAY = date.today()
YESTERDAY = TODAY - timedelta(days=1)


def check_stock_variation(open_p: float, close_p: float):
    diff_perc_num = round((1 - open_p / close_p) * 100)

    if diff_perc_num > 0:
        up_down = "🔼"
    else:
        up_down = "🔽"

    if abs(diff_perc_num) >= 3:
        news_params = {
            "qInTitle": COMPANY_NAME,
            "from": YESTERDAY,
            "to": TODAY,
            "language": "en",
            "sortBy": "popularity",
            "apiKey": NEWS_API_KEY,
        }

        url_news = 'https://newsapi.org/v2/everything'
        r_news = requests.get(url=url_news, params=news_params)
        r_news.raise_for_status()
        articles = r_news.json()["articles"]

        formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_perc_num}%\nHeadline: {article['title']}. \n"
                              f"Brief: {article['description']}" for article in
                              articles[-3:]]

        for article in formatted_articles:
            print(article)


alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": ALPHA_API_KEY,
}

url_stock = 'https://www.alphavantage.co/query'
r_stocks = requests.get(url=url_stock, params=alpha_params)
r_stocks.raise_for_status()
data_stocks = r_stocks.json()["Time Series (Daily)"]
data_list_stocks = [value for (key, value) in data_stocks.items()]
# yesterday_data
yesterday_data = data_list_stocks[0]
yesterday_closing_price = float(yesterday_data["4. close"])
# before_yesterday_data
before_yesterday_data = data_list_stocks[1]
before_yesterday_opening_price = float(yesterday_data["1. open"])

check_stock_variation(open_p=before_yesterday_opening_price, close_p=yesterday_closing_price)
