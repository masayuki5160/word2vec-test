# word2vec-test

# Usage

```
$ git clone git@github.com:masayuki5160/word2vec-test.git
$ cd word2vec-test

# Dockerfileからmasayuki5160/python3と名前をつけdocker imageを作成
$ docker build -t masayuki5160/python3 .

# 作成したdocker image(masayuki5160/python3)をstart
$ docker run -v $(pwd):/home/word2vec-test/  -it masayuki5160/python3 /bin/bash 

# modelを利用する
$ python createModel.py 
```

# Appendix

- [15分でできる日本語Word2Vec](https://qiita.com/makaishi2/items/63b7986f6da93dc55edd)
