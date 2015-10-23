#coding:utf-8
'''
Created on 2015年10月23日

@author: Joanna
'''
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
#首先构建一个PorterStemmer对象
ps=PorterStemmer()
#列举一个例子
example_sentece="It is important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
#切分词语
words=word_tokenize(example_sentece)
#依次输出
for w in words:
    print ps.stem(w)
'''
结果形如：
It
is
import
to
be
pythonli
while
you
are
python
with
python
.
All
python
have
python
poorli
at
least
onc
.
'''
