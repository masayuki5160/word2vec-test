# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import gensim

model = gensim.models.Word2Vec.load('sanshiro.model')
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
   return 'Hello flask'

# hoge
@app.route('/getVector/<string:word>')
def getSimilar(word):
	similarWords = model.most_similar(word)
	words = []
	for word in similarWords:
		words.append({'word':word[0], 'value':word[1]})
	return jsonify({'words': words})

#エラー時のリターン
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

#サーバー起動
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)