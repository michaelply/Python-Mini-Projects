from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://www.basketball-reference.com/leagues/NBA_2022_leaders.html"

# Collect HTML data
html = urlopen(url)

# Create beautiful soup object from HTML
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

table_tags = soup.find_all("table")

def get_nba_leaders_dict():
    all_leaders = {}

    for table in table_tags:
        caption = table.find_all("caption")
        rank_tags = table.find_all("td", attrs={"class": "rank"})
        name_tags = table.find_all("td", attrs={"class": "who"})
        value_tags = table.find_all("td", attrs={"class": "value"})

        category = caption[0].string.lower()

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

    return all_leaders

def save_nba_leaders_df_as_csv(all_leaders_dict):
    for key in all_leaders_dict.keys():
        df = all_leaders_dict[key]
        if key == "box plus/minus":
            table_name = "box plus minus"
        elif key == "offensive box plus/minus":
            table_name = "offensive box plus minus"
        elif key == "defensive box plus/minus":
            table_name = "defensive box plus minus"
        else:
            table_name = key
        df.to_csv(f"nba_leaders_data/{table_name}.csv", index = False)


