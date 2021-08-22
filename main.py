from bs4 import BeautifulSoup as bs
from IPython.display import Image
from requests import get

def take_img(link):
    img = get(link)

def take_link(section, url):
    """get link, and process other links with title."""
    response = get(section)
    soup = bs(response.text, 'html.parser')
    divs = soup.find_all('div', attrs={'class': 'css-10wtrbd'})
    links = [(link.h2.a.get_text(), url+link.h2.a.get('href')) for link in divs]
    if not links:
        h2s = soup.find_all('h2', attrs={'css-6i5eci e1cjqcdm3'})
        links = [(h2.a.get_text(), url+h2.a.get('href')) for h2 in h2s]
        return links
    return links

def new(link):
    """Extract from link: title,"""
    link = get(link)
    soup = bs(link.text, 'html.parser')
    # Extract title
    title = soup.find('h1', attrs={'data-testid': 'headline'})
    copete = soup.find('p')
    epigrapho = soup.find('figcaption', attrs={'class': 'css-13o4bnb e18f7pbr0'})
    body = soup.find_all('p', attrs={'class': 'css-axufdj evys1bk0'})
    bodys = [line.get_text() for line in body]
    if not body:
        body = soup.find_all('p', attrs={'class': 'css-iynevi evys1bk0'})
        bodys = [line.get_text() for line in body]


def main():
    url = 'https://nytimes.com'
    response = get(url)
    soup = bs(response.text, 'html.parser')
    sections = soup.find_all('li', attrs={'data-testid': 'mini-nav-item'})
    links = [(link.a.get_text(), url+link.a.get('href')) for link in sections]
    for link in links:
        print(link[0])
        links = take_link(link[1], url)
        for link in links:
            new(link[1])


if __name__ == '__main__':
    main()
