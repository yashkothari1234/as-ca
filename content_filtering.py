from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

df1 = pd.read_csv('articles.csv')
df1 = df1[df1['soup'].notna()]

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

df1.apply(clean_data)

def create_soup(x):
    return ' '.join(x['eventType']) + ' ' + ' '.join(x['contentType'])
df1['soup'] = df1.apply(create_soup, axis=1)


count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df1['title'])


cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

del df1['level_0']
df1 = df1.reset_index()
indices = pd.Series(df1.index, index=df1['contentId'])

def get_recommendations(title, cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    article_indices = [i[0] for i in sim_scores]
    return df1['title'].iloc[article_indices]
