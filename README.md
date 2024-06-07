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

Итоговый датасет можно посмотреть [здесь](https://drive.google.com/file/d/1-V99uzwP5wY_SgPmIWABUh03u1W9LZqq/view?usp=drive_link)

### Цель проекта

Научиться предсказывать по паре вопрос-ответ со StackOvefrlow, насколько ответ релевантен для данного вопроса, и будет ли ответ одобрен автором,  попробовать использовать несколько различных подходов.

### Метрики

Для задачи предсказания уровня релевантности ответа использовался MSE.
Для задачи предсказания статуса одобрения, использовался f1-score.

### Результаты

Для задачи предсказания релевантности:

- LinearRegression - 23.0023
- DecisionTreeRegressor - 0.2756
- CatBoost - 0.1383
- XGBoost - 0.1383

Для задачи определения статуса ответа

- LogisticRegression - 0.0103
- DecisionTreeClassifier - 0.1619
- CatBoost - 0.0121



