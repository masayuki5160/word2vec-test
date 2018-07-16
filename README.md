# word2vec-test

# Usage

```
$ git clone git@github.com:masayuki5160/word2vec-test.git
$ cd word2vec-test

# build docker image from Dockerfile
$ docker build -t masayuki5160/python3 .

# run docker image(masayuki5160/python3)
$ docker run -v $(pwd):/home/word2vec-test/ -p 5000:5000 -it masayuki5160/python3 /bin/bash

# generate model, and save it. 
$ python createModel.py

# use model
$ python useModel.py

# start api server
$ python webapi.py
```

if you access "http://localhost:5000/similar/男", you can see similar word like below.
```
{
  "words": [
    {
      "value": 0.41406938433647156, 
      "word": "じいさん"
    }, 
    {
      "value": 0.35695937275886536, 
      "word": "迷子"
    }, 
    {
      "value": 0.32412219047546387, 
      "word": "コート"
    }, 
    {
      "value": 0.31509068608283997, 
      "word": "女"
    }, 
    {
      "value": 0.31481245160102844, 
      "word": "ただ"
    }, 
    {
      "value": 0.3141239583492279, 
      "word": "あっち"
    }, 
    {
      "value": 0.3029976487159729, 
      "word": "連中"
    }, 
    {
      "value": 0.29525405168533325, 
      "word": "便所"
    }, 
    {
      "value": 0.2852158546447754, 
      "word": "はやす"
    }, 
    {
      "value": 0.274425208568573, 
      "word": "あぐら"
    }
  ]
}
```

# Appendix

- [青空文庫のデータを利用してWord2Vecを試してみた(Dockerfileつき)](https://qiita.com/masayuki5160/items/a5f442e0e21bc0652f49)
