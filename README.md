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
[
  [
    "じいさん", 
    0.38273391127586365
  ], 
  [
    "あぐら", 
    0.3271724581718445
  ], 
  [
    "コート", 
    0.3263967037200928
  ], 
  [
    "女", 
    0.3059423565864563
  ], 
  [
    "着物", 
    0.30374130606651306
  ], 
  [
    "玩具", 
    0.2950008809566498
  ], 
  [
    "はやす", 
    0.29134976863861084
  ], 
  [
    "制服", 
    0.2833733558654785
  ], 
  [
    "袴", 
    0.2719964385032654
  ], 
  [
    "ふく", 
    0.268212229013443
  ]
]
```

# Appendix

- [青空文庫のデータを利用してWord2Vecを試してみた(Dockerfileつき)](https://qiita.com/masayuki5160/items/a5f442e0e21bc0652f49)
