import requests
from bs4 import BeautifulSoup

import os
import re
import time
import pickle
import numpy as np
import pandas as pd


if __name__ == '__main__':
    CLEANR = re.compile('<.*?>') 

    def cleanhtml(raw_html):
        cleantext = re.sub(CLEANR, '', raw_html)
        return cleantext

    df = pd.DataFrame({'text' : [], 'type' : [], 'rank' : [], 'accepted' : [], 'answers_size' : []})
    out_path = 'data/data{}.csv'
    questions_data = 'data/page_links.pkl'
    main_url = 'https://stackoverflow.com'
    delaying_time = 0.1
    start_id = 0

    with open(questions_data, 'rb') as file:
        questions_urls = pickle.load(file)

    for i in range(start_id, len(questions_urls)):
        question_url = main_url + questions_urls[i]
        response = requests.get(question_url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        question_div = soup.find('div', {'id': 'question'})
        question_text = question_div.find('div', {'class': 's-prose'})
        question_text = cleanhtml(question_text.text).replace('\n', ' ')
        question_rank = int(question_div.find('div', {'class': 'js-vote-count'}).text.strip())
        
        answers_div = soup.find_all('div', {'class': 'answer'})
        df = pd.concat((df, pd.DataFrame({'text' : [question_text], 'type' : [0], 'c' : [question_rank], 'accepted' : [0], 'answers_size' : [len(answers_div)]})), ignore_index=True)

        for answer_div in answers_div:
            answer_rank = int(answer_div.find('div', {'class': 'js-vote-count'}).text.strip())
            answer_text = answer_div.find('div', {'class': 's-prose'})
            answer_text = cleanhtml(answer_text.text).replace('\n', ' ')
            answer_text = answer_text.replace('\r', ' ')
            answer_text = answer_text.replace('\l', ' ')
            accepted = 'd-none' not in answer_div.find('div', {'class': 'js-accepted-answer-indicator'})['class']
            
            df = pd.concat((df, pd.DataFrame({'text' : [answer_text], 'type' : [1], 'rank' : [answer_rank], 'accepted' : [accepted], 'answers_size' : [0]})), ignore_index=True)

        time.sleep(delaying_time)
        
        if i % 10 == 0:
            if len(answers_div) == 0:
                print(question_url)
            print(i, '/', len(questions_urls))
        if i % 1000 == 0:
            df.to_csv(out_path.format(i))

    df.to_csv(out_path)

