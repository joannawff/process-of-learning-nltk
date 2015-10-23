#coding:utf-8
'''
Created on 2015年10月12日

@author: Administrator
'''
from nltk.probability import FreqDist
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
fd=FreqDist()
for text in gutenberg.fileids():
    for word in gutenberg.words(text):
        fd.inc(word)
ranks=[]
freqs=[]
for rank,word in enumerate(fd):
    ranks.append(rank+1)
    freqs.append(fd[word])
plt.loglog(ranks,freqs)
plt.xlabel('frequency(f)',fontsize=14,fontweight='bold')
plt.ylabel('rank(r)',fontsize=14,fontweight='bold')
plt.grid(True)
plt.show()
