from asyncio import exceptions
import requests
from bs4 import BeautifulSoup
import re

def get_soup_page(url_page):
    """Converts URL into a BeautifulSoup object.
    Args:
        url_page (_type_): takes a URL page as input parsed as a string.
    Returns:
        _type_: returns a BeautifulSoup object.
    """
    response = requests.get(url_page)
    page = BeautifulSoup(response.content, 'html.parser')
    return page

def more_pages(soup_object):
    try:
        if soup_object.find(attrs="c-title c-title--subline").get_text().strip()=='No Results found':
            return False
        else:
            return True
    except:
        return True

def read_topics(path_to_file):
    topics = []
    exceptions= {  "alcohol":"Alcohol",
                    "candidate-biography": "candidates-biography",
                    "jan.-6": "jan-6",
                    "message-machine-2010":"message-machine",
                    "negative-campaigning": "campaign-advertising",
                    "polls-and-public-opinion": "polls",
                    "race-and-ethnicity": "race-ethnicity",
                    "regulation":"market-regulation",
                    "tampa-bay-10-news": "10-news-tampa-bay"
                }
    with open(path_to_file, "r") as lines:
        for line in lines.readlines():
            line = line.strip()
            line = re.sub(" ", "-", line)
            try:
                line = exceptions[line.lower()]
            except KeyError:    
                line = line.lower()
                
            topics.append(line)
            
    return topics


