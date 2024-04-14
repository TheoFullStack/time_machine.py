import datetime
from bs4 import BeautifulSoup
import requests

#EXAMPLE: "https://www.billboard.com/charts/hot-100/2000-08-12/"

#setting up time
time_input = input("What date do you want to travel? YYYY-MM-DD:  ")
time= datetime.datetime.strptime(time_input, '%Y-%m-%d')
year = time.year
month = str(time.month).zfill(2)
day = str(time.day).zfill(2)

#setting up URL
URL = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"

#ESTABLISH CONNECTION
response = requests.get(url=URL)
response.raise_for_status()
webpage = response.text

#SET UP BS4
soup = BeautifulSoup(webpage,"html.parser")

li_list= soup.select(selector="li h3",id="title-of-a-story")
titles_list = []
for item in li_list:
    h3 = item.getText().strip()
    titles_list.append(h3)
song_list = [item for item in titles_list if '\n' not in item]
print(song_list)