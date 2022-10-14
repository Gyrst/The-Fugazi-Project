"""
@Gyrst - created in September 2022

When running the politifact scraper make sure to:
1) specify and check that the path for the destination directory is correct.
2) Add a title descriptive of what has been fetched.
3) change "topics" to the desired topics that you would like to fetch. You can add or remove topics to the topcs.txt file
"""

import re
import pandas as pd
from functions import *
from datetime import date

#Remember to specify title to avoid overwriting existing files
title = "_alltopics_"
original_topics = ['climate-change', 'environment', 'abortion', 'coronavirus', 'elections', 'terrorism', 'ukraine']
topics = read_topics("src/topics.txt")
data = []

for topic in topics:
    
    #In order to avoid scraping the topics already scraped earlier.
    if topic in original_topics:
        continue
    
    page_number = 1
    base_url = 'https://www.politifact.com/factchecks/list/?page={page_number}&category={topic}'.format(page_number=page_number, topic=topic)
    print("Currently running for", topic)
    
    while more_pages(get_soup_page(base_url)):
        
        #Clause to avoid that it continues to load next pages even though there aren't any more pages.
        if not more_pages(get_soup_page(base_url)):
            print("hit page limit at:", page_number, "for topic:", topic)
        
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

                #retrieve truth value (e.g., "barely-true")
                truth_value = str(lst_items[i].find_all(attrs={'m-statement__meter'})).split("<img alt=")[1].split(" ")[0].strip("\"")
                
                #retrieve the origin of the claim (e.g., instagram posts, fox news, joe biden)
                origin = soup_object.find(attrs={"m-statement__meta"}).get_text().strip().splitlines()[0]
                
                #retrieve date for when the fake news started spreading
                date_raw = lst_items[i].find_all(attrs={"m-statement__desc"})[0].get_text().strip()
                stated_on = re.search("([^\s]+)\s+\d{1,2}.\s20\d\d", date_raw)[0]
                
                
                news_article = [claim, origin, url, truth_value, stated_on, topic]
                
                # printing the first set from each iteration in the output to stay informed on the progress made
                if i==1:
                    print(news_article)
                
                data.append(news_article)
                
        except:
            print("Error occured at", page_number, base_url)
        page_number += 1
        
    
    
df = pd.DataFrame(data)
print(df)
df = df.rename({df.columns[0]:'claim', df.columns[1]:'origin', df.columns[2]:'URL', df.columns[3]:'truth_value', df.columns[4]:'stated_on',df.columns[5]:'topic'}, axis=1)

path = "data/politifact/"
csv_title = "politifact_scrape{title}{date}.csv".format(title=title, date=str(date.today().strftime("%d%m%Y")))


print(csv_title)
df.to_csv(path+csv_title)
df.to_csv(csv_title)
