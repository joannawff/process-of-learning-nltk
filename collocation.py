#coding:utf-8
'''
Created on 2015年10月11日
测试NLTK的collocation模块
@author: Joanna
'''
from nltk.corpus import stopwords,webtext
from nltk.collocations import BigramCollocationFinder,BigramAssocMeasures
from nltk.probability import FreqDist
from nltk.book import text1
from pip._vendor.distlib.resources import finder
from nltk.metrics import BigramAssocMeasures, spearman_correlation, ranks_from_scores
from nltk.corpus import stopwords, webtext

scorer = BigramAssocMeasures.likelihood_ratio
compare_scorer = BigramAssocMeasures.raw_freq
ignored_words = stopwords.words('english')
word_filter = lambda w: len(w) < 3 or w.lower() in ignored_words
for file in webtext.fileids():
    words = [word.lower()
             for word in webtext.words(file)]
    cf = BigramCollocationFinder.from_words(words)
    cf.apply_freq_filter(3)
    cf.apply_word_filter(word_filter)
    print(file)
    print('\t', [' '.join(tup) for tup in cf.nbest(scorer, 15)])
    print('\t Correlation to %s: %0.4f' % (compare_scorer.__name__,
                                            spearman_correlation(
                                            ranks_from_scores(cf.score_ngrams(scorer)),
                                            ranks_from_scores(cf.score_ngrams(compare_scorer)))))
        
'''
#from nltk.util import bigrams
bigram_measures=BigramAssocMeasures()
trigram_measure=BigramAssocMeasures()
finder=BigramCollocationFinder.from_words("grail.txt")
print finder.nbest()
#filter_stopwords = lambda x:len(x) < 3 or x in stopwords.words("english")
#print filter_stopwords
#words= (w.lower() for w in webtext.words("grail.txt"))
#bcf = BigramCollocationFinder.from_words(words)
#bcf.apply_word_filter(filter_stopwords)
#print bcf.nbest(BigramAssocMeasures.likelihood_ratio,10)
#print list(bigrams(['more','is','said','than','done']))
'''
'''
#词频统计
fdist1=FreqDist(text1)
print fdist1['whale']
'''

