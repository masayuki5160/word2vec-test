# word2vec-test

# Usage

```
$ git clone git@github.com:masayuki5160/word2vec-test.git
$ cd word2vec-test

# build docker image from Dockerfile
$ docker build -t masayuki5160/python3 .

# run docker image(masayuki5160/python3)
$ docker run -v $(pwd):/home/word2vec-test/  -it masayuki5160/python3 /bin/bash 

# generate model, and save it. 
$ python createModel.py
```

# Appendix

- [15分でできる日本語Word2Vec](https://qiita.com/makaishi2/items/63b7986f6da93dc55edd)
