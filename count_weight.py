#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import jieba
import jieba.posseg as pseg
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer

jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('userdict.txt')

class count_weight:
    
    def __init__(self):
        #variable
        self.novel = []
        self.tokenized = []

    def readCSV(self):
        with open('novel.csv', 'r', newline='', encoding='utf-8') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                self.novel.append({'name': row['name'], 'content': row['content']})
        return self.novel
    
    def tokenize_novel(self):
        for i in range(len(self.novel)):
            tmp = jieba.cut(self.novel[i]['content'])
            self.tokenized.append(' '.join(tmp))
        return self.tokenized
            


# In[2]:


#test code
count_weight = count_weight()
count_weight.readCSV()
count_weight.tokenize_novel()
#print(count_weight.novel[0]['tokenized'])

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(count_weight.tokenized)
#印出文章數量、詞彙數量
print(tfidf.shape)
#印出詞彙、權重
words = vectorizer.get_feature_names()
for i in range(len(count_weight.tokenized)):
    print ('----Document %d----' % (i))
    for j in range(len(words)):
        if tfidf[i,j] > 1e-5:
              print (words[j], tfidf[i,j])


# In[ ]:




