# word_cloud
word_cloudというものが面白そうだったので仲良しグループラインのテキストを利用して遊んでみた

### 適当な説明でごめんなさい←超重要

## 環境設定
mac OS Catalina 10.15.1 ver.

Python 3.7.4

## 参考リンク
[モチベーションとなった記事]

[【Python】嵐の歌詞をWordCloudで可視化して、結成20年でファンに伝えたかったことを紐解いてみた](https://qiita.com/yuuuusuke1997/items/122ca7597c909e73aad5)

[コードを参考した記事]

[Word Cloud を使ってテキストマイニングしてみる](http://cedro3.com/ai/word-cloud/)

## 利用方法
```
python make_word_cloud.py
```
を実行すればテキストファイルから文を読み取り以下のような画像を吐き出してくれる


![word_cloud](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQrsLqxSrxhys6EQ0FDDKPo1q_K4CpPn4Irep8T5rngVZhbVfTk "サンプル")
## 自分で変更する必要がある行
```
6行目: text_file = open("path/to/file")
```
ここに読み込んで欲しいテキストファイルを指定する
とりあえずテキストファイルなら何でもオッケー!!!!!

```
27行目: stop_words = ['さん','そう','です','ます']
```
stop_wordsでは表示させたくない単語を指定することができる

```
29行目: fpath = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'
```
fpathにはフォントを指定する(日本語を表示させたい時は日本語対応しているフォントを選ぼう）

## p.s
* これからもこういった遊びを取り入れつつ楽しく自然言語処理を学んでいきたいですね

* 実生活に自然言語処理を共存させるとめちゃめちゃ楽しい事に気付きました

* モチベーションがupupup





