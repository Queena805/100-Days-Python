from bs4 import BeautifulSoup
import requests

URL = "https://www.imdb.com/list/ls500939644/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=62e5542a-e7b7-4016-97fd-14f676aa138f&pf_rd_r=XCPEH1V5YPKMS40JC5TB&pf_rd_s=center-3&pf_rd_t=60601&pf_rd_i=whats-on-tv&ref_=fea_wot_wot_juneTVcal_ctr_sm"
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")


# print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="lister-item-header")
# print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]
for item in movie_titles:
    print(item)


# movies = movie_titles[::-1]

# with open("movies.txt", mode="w")as file:
#     for movie in movies:
#         file.write(f"{movie}\n")


with open("tv.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

