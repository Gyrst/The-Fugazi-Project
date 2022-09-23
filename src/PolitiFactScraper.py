import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import time

topics = ['climate-change', 'environment', 'abortion', 'coronavirus', 'elections', 'terrorism', 'ukraine']

base_url = 'https://www.politifact.com/factchecks/list/?page={page_number}&category={topic}'.format(page_number=1, topic=topics[0])



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



print(base_url)

so = get_soup_page(base_url)

print(so)

# class PolitiFactScraper:
    
#     def __init__(self, topic):
        
    
    
#     def get_soup_page(self, url_page):
#         """Converts URL into a BeautifulSoup object.

#         Args:
#             url_page (_type_): takes a URL page as input parsed as a string.

#         Returns:
#             _type_: returns a BeautifulSoup object.
#         """
#         response = requests.get(url_page)
#         page = BeautifulSoup(response.content, 'html.parser')
#         return page
