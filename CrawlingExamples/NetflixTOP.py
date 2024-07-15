#파이썬_WordCloud 넷플릭스 인기있는 tv쇼/영화 캐스팅 배우 순위(워드클라우드)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS

df_netflix=pd.read_csv('C:\\Users\\mine\\data\\netflix_titles.csv')

#워드 클라우드 설정
mpl.rcParams['font.size']= 15
mpl.rcParams['savefig.dpi']= 100
mpl.rcParams['figure.subplot.bottom']= .1

#워드 클라우드 정의
plt.figure(figsize = (15,15))

stopwords = set(STOPWORDS)

wordcloud = WordCloud(background_color='black',
                    stopwords=stopwords,
                    max_words=1000,
                    max_font_size=120,
                    random_state=42).generate(str(df_netflix['cast']))

print(wordcloud)

fig = plt.figure(1)
plt.imshow(wordcloud)
plt.title("word coloud - Casts")
plt.axis('off')
plt.show()