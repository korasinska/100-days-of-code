import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

#get website content
movies_web = requests.get(URL)
web_content = movies_web.text

#parse this content
soup = BeautifulSoup(web_content, "lxml")

#find all h3 tags with title class in the content
web_titles = soup.select("h3.title")

#create list of pure titles
titles = [title.getText() for title in web_titles]

#sort and optionally correct titles
#corrected_titles = [title.replace("12:", "12)") for title in titles]
#sorted_list = sorted(corrected_titles, key=lambda x:int(x.split(")")[0])) or easier:
sorted_titles = titles[::-1]

#write every title to a movie.txt file
with open("movies.txt", "w") as file:
    for title in sorted_titles:
        file.write(f"{title}\n")
