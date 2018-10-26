#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv
import jieba
import jieba.posseg as pseg
import json

jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('userdict.txt')

'''
tokenize the novel, remove useless words
and store in json
'''


# In[29]:


class tokenize_to_json:
    def __init__(self):
        #variable
        self.novel = []
        self.tokenized = []
    
    def readCSV(self):
        with open('novel.csv', 'r', newline='', encoding='utf-8') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                content = row['content'].replace('\r', ' ')
                self.novel.append({'name': row['name'], 'content': content})
        return self.novel
    
    def tokenize_novel(self):
        stop_flags = {'x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r'}
#         #test code
#         for i in range(2):
        for i in range(len(self.novel)):
            tmp = []
            terms = pseg.cut(self.novel[i]['content'])
            for term, flag in terms:
                if flag not in stop_flags:
                    tmp.append(term)
            print('complete tokenized ch', i)
            self.tokenized.append(tmp)
        return self.tokenized

    def write_json(self):
        with open('doc_term_list.json', 'w') as file:
            json.dump(self.tokenized, file)
        return
            
    def read_json(self):
        doc_term_list = []
        with open('doc_term_list.json', 'r') as file:
            doc_term_list = json.load(file)
        return doc_term_list
        


# In[33]:


#test code
# ttj = tokenize_to_json()
# ttj.readCSV()
# ttj.tokenize_novel()
# ttj.write_json()
# dtl = ttj.read_json()

