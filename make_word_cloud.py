#.txtファイルを読み取りword_cloudで画像を生成
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_file = open("kawamura.txt")
full_text = text_file.read()
full_text= full_text.replace("\n","")

print(full_text)
t = Tokenizer()
tokens = t.tokenize(full_text)


word_list=[]
for token in tokens:
    word = token.surface
    partOfSpeech = token.part_of_speech.split(',')[0]
    partOfSpeech2 = token.part_of_speech.split(',')[1]

    if partOfSpeech == "名詞":
        if (partOfSpeech2 != "非自立") and (partOfSpeech2 != "代名詞") and (partOfSpeech2 != "数"):
            word_list.append(word)

words_wakati=" ".join(word_list)
print(words_wakati)
stop_words = ['さん','そう','安井','谷口','尊師','準尊師','新尊師','川村','中津'
             ,'和泉','りょうすけ','よしと','かずき','森田','上田','中川','中谷']
fpath = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'
wordcloud = WordCloud(
    font_path=fpath,
    width=900, height=600,   # default width=400, height=200
    background_color="white",   # default=”black”
    stopwords=set(stop_words),
    max_words=500,   # default=200
    min_font_size=4,   #default=4
    collocations = False   #default = True
    ).generate(words_wakati)

plt.figure(figsize=(15,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("word_cloud.png")
plt.show()
