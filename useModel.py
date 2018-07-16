import gensim

model = gensim.models.Word2Vec.load('sanshiro.model')

# ベクトルを取り出す
print(model["世間"])

# 類似の単語を探す
print(model.most_similar("日本"))

# 単語の加減を計算して類似の単語を探す
print(model.most_similar(positive=['東京'], negative=['人']))
