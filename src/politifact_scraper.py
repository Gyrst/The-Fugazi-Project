import re
import pandas as pd
from scraper_functions import *
from datetime import date


topics = ['climate-change', 'environment', 'abortion', 'coronavirus', 'elections', 'terrorism', 'ukraine']
#topics = read_topics("src/topics.txt")
data = []

for topic in topics:
    page_number = 1
    base_url = 'https://www.politifact.com/factchecks/list/?page={page_number}&category={topic}'.format(page_number=page_number, topic=topic)
    print("Currently running for", topic)
    
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

                #retrieve truth value (e.g., "barely-true")
                truth_value = str(lst_items[i].find_all(attrs={'m-statement__meter'})).split("<img alt=")[1].split(" ")[0].strip("\"")
                
                #retrieve the origin of the claim (e.g., instagram posts, fox news, joe biden)
                origin = soup_object.find(attrs={"m-statement__meta"}).get_text().strip().splitlines()[0]
                
                #retrieve date for when the fake news started spreading
                date_raw = lst_items[i].find_all(attrs={"m-statement__desc"})[0].get_text().strip()
                
                stated_on = re.search("([^\s]+)\s+\d{1,2}.\s20\d\d", date_raw)[0]
                
                
                news_article = [claim, origin, url, truth_value, stated_on, topic]
                
                if page_number==1:
                    print(news_article)
                
                data.append(news_article)
                
        except:
            print("Error occured at", page_number, base_url)
        page_number += 1
        
    
    
df = pd.DataFrame(data)
print(df)
df = df.rename({df.columns[0]:'claim', df.columns[1]:'origin', df.columns[2]:'URL', df.columns[3]:'truth_value', df.columns[4]:'stated_on',df.columns[5]:'topic'}, axis=1)

#path = "data/politifact/"
csv_title = "politifact_scrape_7t_{date}.csv".format(date=str(date.today().strftime("%d%m%Y")))


print(csv_title)
df.to_csv(csv_title)
