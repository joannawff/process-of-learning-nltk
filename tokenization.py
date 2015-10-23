#coding:utf-8
'''
Created on 2015年10月23日

@author: Joanna
'''
#分词分为句级和词级
from nltk.tokenize import sent_tokenize,word_tokenize
#首先举例，一句话
example_text="Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue and you can't eat cardboard."
#一般的分词是通过空格split，然而当出现如Mr. Smith时，无法将其正确分出
#打印分句结果
print sent_tokenize(example_text,'english')#这里正常为sent_tokenize(text,language),language可省略
'''
结果形如：
['Hello Mr. Smith, how are you doing today?', 
'The weather is great and Python is awesome.', 
"The sky is pinkish-blue and you can't eat cardboard."]
'''
#打印分词结果
print word_tokenize(example_text)#这里的language就省略了
'''
结果形如：
['Hello', 'Mr.', 'Smith', ',', 'how', 'are', 'you', 'doing', 'today', '?', 
'The', 'weather', 'is', 'great', 'and', 'Python', 'is', 'awesome', '.', 
'The', 'sky', 'is', 'pinkish-blue', 'and', 'you', 'ca', "n't", 'eat', 'cardboard', '.']
'''
