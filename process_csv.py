import re
import spacy
import pandas as pd


def text_process(text, nlp):
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(' +', ' ', text)
    text = text.lstrip()
    text = text.rstrip()
    text = text.lower()

    doc = nlp(text)
    filtered_words = [token.lemma_ for token in doc if not token.is_stop]
    clean_text = ' '.join(filtered_words)
    return clean_text


if __name__ == '__main__':
    data_path = 'data/data.csv'
    processed_data_path = 'data/processed_data.csv'

    df = pd.read_csv(data_path)
    df_main = pd.DataFrame({'text': [], 'rank': [], 'accepted' : []}) 
    nlp = spacy.load("en_core_web_sm")

    pos = 0
    separator = ' $sep$ '
    while pos < len(df):
        if df.iloc[pos].isna().any():
            if not df.iloc[pos].isna()['answers_size']:
                pos += int(df['answers_size'][pos]) + 1
            else:
                pos += 1
            continue
                
        steps = int(df['answers_size'][pos])
        question = text_process(df['text'][pos], nlp)
        
        max_rank = 0.0
        for i in range(1, steps + 1):
            if df.iloc[pos + i].isna().any():
                continue

            max_rank = max(df['rank'][pos + i], max_rank)
        
        if max_rank != 0.0:
            for i in range(1, steps + 1):
                if df.iloc[pos + i].isna().any():
                    continue

                question_answer = question + separator + text_process(df['text'][pos + i], nlp)
                rank = df['rank'][pos + i] / max_rank
                accepted = int(df['accepted'][pos + i])
                
                df_temp = pd.DataFrame({'text': [question_answer], 'rank': [rank], 'accepted' : [accepted]})
                df_main = pd.concat((df_main, df_temp), ignore_index=True)
            
        pos += steps + 1
        
        if pos % 100 == 0:
            print(pos, '/', len(df))
            
    df_main.to_csv(processed_data_path)