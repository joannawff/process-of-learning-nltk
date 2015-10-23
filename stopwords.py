#coding:utf-8
'''
Created on 2015年10月23日

@author: Joanna
'''
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#举一句话
example_sentence="This is an example showing off stop word filtration."
#查找英文中的停顿词
stop_words=set(stopwords.words('english'))
#对例句进行切词
words=word_tokenize(example_sentence)
#用于保存过滤后的单词
filtered_sentence=[]
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
#输出非停顿词
print filtered_sentence
#结果如：['This', 'example', 'showing', 'stop', 'word', 'filtration', '.']
'''
输出所有的限定词
stop_words=set(stopwords.words('English'))
print stop_words
'''
