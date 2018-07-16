# Janomeのロード
from janome.tokenizer import Tokenizer
import codecs
import re
# Word2Vecライブラリのロード
from gensim.models import word2vec

# ファイル読込み、内部表現化
f = codecs.open('sanshiro.txt', "r", "sjis")
text = f.read()
f.close()

# ヘッダ部分の除去
text = re.split('\-{5,}',text)[2]
# フッタ部分の除去
text = re.split('底本：',text)[0]
# | の除去
text = text.replace('|', '')
# ルビの削除
text = re.sub('《.+?》', '', text)
# 入力注の削除
text = re.sub('［＃.+?］', '',text)
# 空行の削除
text = re.sub('\n\n', '\n', text) 
text = re.sub('\r', '', text)

# Tokenneizerインスタンスの生成 
t = Tokenizer()

# テキストを引数として、形態素解析の結果、名詞・動詞原型のみを配列で抽出する関数を定義 
def extract_words(text):
    tokens = t.tokenize(text)
    return [token.base_form for token in tokens 
        if token.part_of_speech.split(',')[0] in['名詞', '動詞']]

#  関数テスト
# ret = extract_words('三四郎は京都でちょっと用があって降りたついでに。')
# for word in ret:
#     print(word)

# 全体のテキストを句点('。')で区切った配列にする。 
sentences = text.split('。')
# それぞれの文章を単語リストに変換(処理に数分かかります)
word_list = [extract_words(sentence) for sentence in sentences]

# 結果の一部を確認 
# for word in word_list[0]:
#     print(word)


# size: 圧縮次元数
# min_count: 出現頻度の低いものをカットする
# window: 前後の単語を拾う際の窓の広さを決める
# iter: 機械学習の繰り返し回数(デフォルト:5)十分学習できていないときにこの値を調整する
# model.wv.most_similarの結果が1に近いものばかりで、model.dict['wv']のベクトル値が小さい値ばかりの 
# ときは、学習回数が少ないと考えられます。
# その場合、iterの値を大きくして、再度学習を行います。

# 事前準備したword_listを使ってWord2Vecの学習実施
model = word2vec.Word2Vec(word_list, size=100,min_count=5,window=5,iter=100)

# 結果の確認1
# 一つ一つの単語は100次元のベクトルになっています。 
# 「世間」のベクトル値を確認します。
print(model.__dict__['wv']['世間'])

# 結果の確認2
# 関数most_similarを使って「世間」の類似単語を調べます 
ret = model.wv.most_similar(positive=['世間']) 
for item in ret:
    print(item[0], item[1])