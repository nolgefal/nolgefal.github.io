# -*- coding: utf-8 -*-
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import math
import MeCab as mc

posid = [2,3,10,12,31,36,38,40,41,42,43,44,45,46,47,48,49,50]
# list stopwords
with open('Japanese_stopword_list.txt', 'r',encoding='utf8') as f:
    stop_words = f.read().splitlines()
    
def mecab_analysis(text):    
    tagger = mc.Tagger('-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd/')
    tagger.parse('')
    node = tagger.parseToNode(text) 
    output = []
    while(node):
        if node.posid in posid and node.surface != "" and node.surface not in stop_words:
#             print(node.surface)#, node.posid, node.feature.split(",")[0]) # get word_type
            output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

def create_wordcloud(frequencies):
    fpath = "HatsukoiFriends-mini.otf"    
    wordcloud = WordCloud(
                            stopwords=set(stop_words),
                            font_path=fpath,
                            background_color="white", relative_scaling = 1.0,
                            min_font_size=4, width=1024, height=768,
                            scale=3, font_step=1, collocations=True, margin=2,
                            ).fit_words(frequencies)
    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


questions = pd.read_csv('./data/questions-2017-10-16.csv', encoding='utf-8', delimiter=',',quotechar='"')
users = pd.read_csv('./data/users-2017-10-16.csv', delimiter="\t", encoding='cp932')
description = []
for e in questions['Category'].unique():
    description.append(mecab_analysis(" ".join(questions['Description'].loc[questions['Category'].isin([e])]))) 


