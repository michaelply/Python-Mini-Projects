from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://www.basketball-reference.com/leagues/NBA_2022_leaders.html"

# collect HTML data
html = urlopen(url)

# create beautiful soup object from HTML
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

table_tags = soup.find_all("table")

for table in table_tags:
    all_leaders = {}

    caption = table.find_all("caption")
    rank_tags = table.find_all("td", attrs={"class": "rank"})
    name_tags = table.find_all("td", attrs={"class": "who"})
    value_tags = table.find_all("td", attrs={"class": "value"})

    category = caption[0].string.lower()
    print(category)

    rank_col = []
    for tag in rank_tags:
        rank = tag.string
        if rank:
            rank_col.append(tag.string[:-1])
        else:
            rank_col.append(rank_col[-1])

    name_col = []
    for tag in name_tags:
        name_col.append(tag.find_all("a")[0].string)

    value_col = []
    for tag in value_tags:
        value_col.append(tag.string)

    table_dict = {"name": name_col, "rank": rank_col, "value": value_col}
    df = pd.DataFrame(table_dict)
    all_leaders[category] = df

print(all_leaders.keys())





#
# caption_tags = table_tags.find_all("td")
# print(caption_tags)

