import requests, re
from bs4 import BeautifulSoup
import pandas as pd
from scraper_functions import *

topics = ['climate-change', 'environment', 'abortion', 'coronavirus', 'elections', 'terrorism', 'ukraine']

data = []

for topic in topics:
    page_number = 1
    base_url = 'https://www.politifact.com/factchecks/list/?page={page_number}&category={topic}'.format(page_number=page_number, topic=topic)
    print("currently running for", topic)
    
    while more_pages(get_soup_page(base_url)):
        if not more_pages(get_soup_page(base_url)):
            print("hit page limit at:", page_number, "for topic:", topic)
        if page_number>100:
            break
        
        try:
            base_url = 'https://www.politifact.com/factchecks/list/?page={page_number}&category={topic}'.format(page_number=page_number, topic=topic)
            
            soup_object = get_soup_page(base_url)
            lst_items = soup_object.find_all(attrs={"o-listicle__item"})
            
            for i in range(len(lst_items)):
                
                #retrieve the claim
                claim = lst_items[i].find_all('a', href=True)[1].get_text().strip()

                #retrieve url
                url_ending = str(lst_items[i].find_all('a', href=True)[1]).split("\">")[0].split("<a href=\"")[1]
                url = "https://www.politifact.com{url_ending}".format(url_ending=url_ending)

                #retrieve truth value e.g., "barely-true"
                truth_value = str(lst_items[i].find_all(attrs={'m-statement__meter'})).split("<img alt=")[1].split(" ")[0].strip("\"")
                
                #retrieve the origin of the claim i.e., instagram posts, fox news, joe biden
                origin = soup_object.find("m-statement__meta")
                
                
                #retrieve date for when the fake news started spreading
                date_raw = lst_items[i].find_all(attrs={"m-statement__desc"})[0].get_text().strip()
                stated_on = re.search("([^\s]+)\s+\d{1,2}.\s20\d\d", date_raw)[0]
                
                news_article = [claim, url, truth_value, stated_on, topic]
                
                data.append(news_article)
        except:
            print("error occured at", page_number, base_url)
        
        page_number += 1

df = pd.DataFrame(data)
df = df.rename({df.columns[0]:'claim', df.columns[1]:'URL', df.columns[2]:'truth_value', df.columns[3]:'stated_on',df.columns[4]:'topic'}, axis=1)

df.to_csv("data/full_scape_0310.csv")
