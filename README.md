# 金庸武俠小說章節相似度計算
### 天龍八部

---
計算每個章節的文章向量，比較相似度，最相似的合併後產生新向量繼續比較，最後將結果繪製成Tree

* Jieba參考資源：https://colab.research.google.com/drive/1KD_U2BOhhWKW9UdhKh_z3lp_EOfh4_I7
* Hierichal Tree 繪圖參考：https://colab.research.google.com/drive/1VXStWmXomJ47e2zmywconho21neVUI62

---
#### 主要程式
* crawler_novel.py
    * 從網頁上抓取小說內容，並寫入csv檔
* tokenize_to_json.py
    * 讀取novel.csv, userdict.txt, dict.txt.big，斷詞並刪除無用詞彙(ex.的、了、標點符號)，並輸出json檔(doc_term_list.json)
* cluster_input.py
    * 處理小說和斷詞，整理成cluster程式的input檔案(data_tf & data_tfidf)
* draw_cluster.py
    * 讀取data_tf & data_idf，繪製成圖(cluster_tf & cluster_idf)

#### 其他檔案
* test_tokenize.ipynb
    * jieba使用方式
* count_weight.ipynb
    * sklearn使用方式
* similarity_of_doc.ipynb
    * gensim使用方式


* 讀取csv檔方法
```
import csv
with open(self.fileName, 'r', newline='', encoding='utf-8') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        #章節名稱
        print(row['name'])
        #章節內容
        print(row['content'])
```

