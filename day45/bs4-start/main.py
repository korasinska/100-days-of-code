from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
articles_text = []
articles_links = []
articles = soup.select("span.titleline > a")

for article in articles:
    text = article.getText()
    articles_text.append(text)
    link = article.get("href")
    articles_links.append(link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.select("span.score")]

largest_vote = max(article_upvotes)
largest_index = article_upvotes.index(largest_vote)
highest_voted_title = articles_text[largest_index]
highest_voted_link = articles_links[largest_index]

print(largest_vote, highest_voted_title, highest_voted_link)