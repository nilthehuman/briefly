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

def get_html_text(url):
    """Download given page and extract main content."""
    try:
        response_text = requests.get(url).text
    except requests.exceptions.RequestException:
        return None
    soup = BeautifulSoup(response_text, 'html.parser')
    text = soup.get_text()
    # A bit of cleanup
    for script in soup(["script", "style"]):
        script.extract()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def get_the_body_only(html):
    """Prune title, header etc. from the raw extract."""
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.body.get_text()
    return body_text
