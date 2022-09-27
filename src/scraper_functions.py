import requests
from bs4 import BeautifulSoup

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
