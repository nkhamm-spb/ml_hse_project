#  Предсказание релевантности ответа на вопрос со StackOverflow
HSE ML course project (2nd year)

### Команда:
- Хамматов Никита

### Установка
```console
foo@bar:~$ pip3 install -r requirements.txt
```

##  Описание данных
Данные были получены напрямую со StackOverflow путем парсинга с помощью библиотеки BeautifulSoup4. 
Код получение ссылок на вопросы [page_url_collection.py](https://github.com/nkhamm-spb/ml_hse_project/blob/main/collect_data.py).
Код получение  вопросов [page_url_collection.py](https://github.com/nkhamm-spb/ml_hse_project/blob/main/page_url_collection.py).

Далее каждый пост обрабатывается, убирается пунктуация, формируется пара вопрос-ответ, и каждому вопросу выставляется ранг, 
как отношение оценки к максимальной оценки ответа на вопрос в посте(то есть самый подходящий ответ имеет ранг 0).

Код обработки данных [process_csv.py](https://github.com/nkhamm-spb/ml_hse_project/blob/main/process_csv.py).

Итоговый датасет можно посмотреть [здесь](https://www.kaggle.com/datasets/datasnaek/mbti-type)
