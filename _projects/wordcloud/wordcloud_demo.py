# -*- coding: utf-8 -*-
#!/usr/bin/env python

# """
# Minimal Example
# ===============
# Generating a square wordcloud from the US constitution using default arguments.
# """

# from os import path
# from wordcloud import WordCloud

# d = path.dirname(__file__)

# # Read the whole text.
# # text = open(path.join(d, '/media/lhlong/01D309ADC81A8610/lhlong/ML/work/self/data/words/sherlock_home.txt')).read()
# text = open(path.join(d, 'question.txt')).read()
# # Generate a word cloud image
# wordcloud = WordCloud().generate(text)

# # Display the generated image:
# # the matplotlib way:
# import matplotlib.pyplot as plt
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# # lower max_font_size
# wordcloud = WordCloud(max_font_size=40).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# # The pil way (if you don't have matplotlib)
# # image = wordcloud.to_image()
# # image.show()

############################################################
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import MeCab as mc

def mecab_analysis(text):
    t = mc.Tagger('-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd/')
    enc_text = text.encode('utf-8') 
    node = t.parseToNode(enc_text) 
    output = []
    while(node):
        if node.surface != "":
            word_type = node.feature.split(",")[0]
            if word_type in ["形容詞", "動詞","名詞", "副詞"]: #noun - verb - adj - adv
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output


def get_wordlist_from_QiitaURL(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    text = soup.body.section.get_text().replace('\n','').replace('\t','')
    return mecab_analysis(text)
    
def create_wordcloud(text):

    fpath = "/home/lhlong/hengo/home/lhlong.github.io/_projects/wordcloud/HatsukoiFriends-mini.otf"
    stop_words = [ 'てる', 'いる', 'なる', 'れる', 'する', 'ある', 'こと', 'これ', 'さん', 'して', \
             'くれる', 'やる', 'くださる', 'そう', 'せる', 'した',  '思う',  \
             'それ', 'ここ', 'ちゃん', 'くん', '', 'て','に','を','は','の', 'が', 'と', 'た', 'し', 'で', \
             'ない', 'も', 'な', 'い', 'か', 'ので', 'よう', '']
    wordcloud = WordCloud(
                            background_color="white",
                            font_path=fpath,
                            relative_scaling = 1.0,
                            min_font_size=4,
                            width=1024,
                            height=768,
                            scale=3,
                            font_step=1,
                            collocations=True,
                            margin=2,
                            stopwords=set(stop_words)
                            ).generate(text)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    

# input get from url
url = "http://qiita.com/t_saeko/items/2b475b8657c826abc114"
wordlist = get_wordlist_from_QiitaURL(url)
# print(" ".join(wordlist).decode('utf-8'))
create_wordcloud(" ".join(wordlist).decode('utf-8'))

#==========================================================
# input is string <get from question file>
questions = '''
私はいつも失敗を犯す人間です

仕事、対人関係、人生の選択にすら失敗なのではと感じる程です。

以前その失敗の一つの為に友人と険悪になり、
それ以来性格を変えたいと思うようになり、意識するようになりました。

しかしどんなに意識してもすぐに気持ちを変えられる事が出来ず、結局引きずってしまいます。

過去にも同じ様な事があった結果、大阪での就職に失敗し徳島に戻り、
現在実家の自営業で仕事をしていますが、
やはり仕事の失敗を繰り返し、険悪になってしまいます。

もう家にすら自分の居場所が無いように感じます。

最近ネットで調べてみると、発達障害の可能性がある事が分かりました。

ですが大阪時代での鬱の疑いの時に結局思い込みと見なされ、向き合ってくれない様に感じた事から相談もできません。

もうどうしたらいいか分かりません。

落ち込みがピークに達すると、いっそ殺してほしい、死にたく無いけど殺してほしい、
むしろ居なくなりたい、この世に居なかった事になりたい、と思う事もあります。

私に解決策はあるのでしょうか
'''
# create_wordcloud(" ".join(mecab_analysis(questions.decode('utf-8'))).decode('utf-8'))

# tokenizer = mecab_analysis(questions.decode('utf-8'))
# for e in tokenizer:
#     print(e.decode('utf-8'))
