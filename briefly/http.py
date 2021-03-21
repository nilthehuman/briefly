"""Download target website content through HTTP."""

import requests
from bs4 import BeautifulSoup

def check_internet_connection():
    """See if this system can access the Web."""
    try:
        response = requests.get('http://vanenet.hu')
    except requests.exceptions.RequestException:
        return False
    return response.status_code == 200

def get_html_body(url):
    """Download given page and extract main content."""
    response_text = requests.get(url).text
    soup = BeautifulSoup(response_text, 'html.parser')
    return soup.body.get_text()
