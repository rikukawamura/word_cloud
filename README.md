# word_cloud
word_cloudというものが面白そうだったので仲良しグループラインのテキストを利用して遊んでみた
適当な説明でごめんなさい

## 利用方法
```
python make_word_cloud.py
```
を実行すればテキストファイルから文を読み取り以下のような画像を吐き出してくれる
![word_cloud](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQrsLqxSrxhys6EQ0FDDKPo1q_K4CpPn4Irep8T5rngVZhbVfTk "サンプル")
## 自分で変更する必要がある行
ここに読み込んで欲しいテキストファイルを指定する
```
6行目: text_file = open("kawamura.txt")
```

stop_wordsでは表示させたくない単語を指定することができる
```
stop_words = ['さん','そう','安井','谷口','尊師','準尊師','新尊師','川村','中津'
             ,'和泉','りょうすけ','よしと','かずき','森田','上田','中川','中谷']
```

fpathにはフォントを指定する(日本語を表示させたい時は日本語対応しているフォントを選ぼう）

```
fpath = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'
```

