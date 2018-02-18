import requests
import urllib
from bs4 import BeautifulSoup
import time

MAX_CRAWL_URL = 25
SLEEP_MIN_PER_REQ = 2
WIKI_URL = "https://en.wikipedia.org"
BEGIN_URL = "https://en.wikipedia.org/wiki/Special:Random"
TARGET_URL = "https://en.wikipedia.org/wiki/Philosophy"

def continue_crawl(search_history, target_url=TARGET_URL):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False

    if len(search_history) > MAX_CRAWL_URL:
        print("The search has gone on suspiciously long, aborting search!")
        return False

    if search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False

    return True

def get_first_a_href(url):
    response = requests.get(url)
    html_text = response.text

    soup = BeautifulSoup(html_text, "html.parser")
    div_tag = soup.find(id="mw-content-text").find(class_='mw-parser-output')

    for child_tag in div_tag.children:
        if child_tag.name != 'p':
            continue

        for p_child_tag in child_tag.children:
            if p_child_tag.name == 'a':
                return urllib.parse.urljoin(WIKI_URL, p_child_tag.get('href'))

    return None

def crawl_wiki_page(begin_url=BEGIN_URL):
    article_chain = [begin_url, ]

    while continue_crawl(article_chain):
        print(article_chain[-1])
        next_url = get_first_a_href(article_chain[-1])
        if not next_url:
            print("We've arrived at an article with no links, aborting search!")
            break

        article_chain.append(next_url)

        time.sleep(SLEEP_MIN_PER_REQ)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        crawl_wiki_page(urllib.parse.urljoin(WIKI_URL, '/wiki', sys.argv[1]))
    else:
        crawl_wiki_page()

