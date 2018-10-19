# 金庸武俠小說章節相似度計算
### 天龍八部

---
計算每個章節的文章向量，比較相似度，最相似的合併後產生新向量繼續比較，最後將結果繪製成Tree

* Jieba參考資源：https://colab.research.google.com/drive/1KD_U2BOhhWKW9UdhKh_z3lp_EOfh4_I7
* Hierichal Tree 繪圖參考：https://colab.research.google.com/drive/1VXStWmXomJ47e2zmywconho21neVUI62

---
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

