from bs4 import BeautifulSoup as bs
from requests import get

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



def main():
    url = 'https://nytimes.com'
    response = get(url)
    soup = bs(response.text, 'html.parser')
    sections = soup.find_all('li', attrs={'data-testid': 'mini-nav-item'})
    links = [(link.a.get_text(), url+link.a.get('href')) for link in sections]
    for link in links:
        print(link[0])
        print(take_link(link[1], url))

if __name__ == '__main__':
    main()
