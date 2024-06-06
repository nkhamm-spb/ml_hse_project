import requests
from bs4 import BeautifulSoup

import time
import pickle
import numpy as np


if __name__ == '__main__':
    out_path = 'data/page_links.pkl'
    pages_url = 'https://stackoverflow.com/questions?tab=votes&page={}'
    num_pages = 550 # We won't use all the questions.
    max_pages = 10000
    delaying_time = 0.5

    selected_pages = np.random.choice(max_pages, num_pages, replace=False) + 1

    page_links = []

    for i, id in enumerate(selected_pages):
        page_url = pages_url.format(id)
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        urls = soup.find_all('a', class_='s-link')
        
        if len(urls) == 0:
            print("here")
        
        for url in urls:
            if 'questions' in url['href'] and 'stackexchange.com' not in url['href']:
                page_links.append(url['href'])

        time.sleep(delaying_time)
        
        if i % 10 == 0:
            print(len(urls))
            print(i, '/', num_pages)

    with open(out_path, 'wb') as file:
        pickle.dump(page_links, file)