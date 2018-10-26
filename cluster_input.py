#!/usr/bin/env python
# coding: utf-8

# In[29]:


from tokenize_to_json import *
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer

'''
build the input data for cluster picture
the format of data is
'all terms\t
\n
chapter names\t each term weight\t
\n'
there are two method：tf and tf-idf
'''

#get all terms of all documents
ttj = tokenize_to_json()
novel = ttj.readCSV()
tokenized = ttj.read_json()

#build dictionary(remove duplicate words)
term = []
for i in range(len(tokenized)):
    term = tokenized[i] + term
term = list(set(term))

def count_tf(n):
    tmp = []
    tmp.append(n['name'])
    for t in term:
        num = n['content'].count(t)
        tmp.append(str(num))
    print(tmp[0])
    return tmp

def count_tfidf():
    all_doc = []
    tmp = []
    for t in tokenized:
        all_doc.append(' '.join(t))
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(all_doc)
    words = vectorizer.get_feature_names()
    for i in range(len(all_doc)):
        tmp.append([])
        print(novel[i]['name'])
        tmp[i].append(novel[i]['name'])
        for j in range(len(words)):
            tmp[i].append(str(tfidf[i, j]))
    return tmp
        


# In[30]:


with open('data_tf', 'w') as f:
    print('write data_tf')
    f.write('\t'.join(term))
    for n in novel:
        tmp = count_tf(n)
        f.write('\n')
        f.write('\t'.join(tmp))
        
with open('data_tfidf', 'w') as f:
    print('write data_tfidf')
    f.write('\t'.join(term))
    lines = count_tfidf()
    for line in lines:
        f.write('\n')
        f.write('\t'.join(line))


# In[51]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:





# In[ ]:





# In[ ]:




