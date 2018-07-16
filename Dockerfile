FROM python:3.6

VOLUME /home/word2vec-test

RUN apt-get update && \
    apt-get -y install sudo vim unzip && \
    pip install --upgrade gensim && \
    pip install janome && \
    wget -O /tmp/794_ruby_4237.zip http://www.aozora.gr.jp/cards/000148/files/794_ruby_4237.zip && \
    unzip /tmp/794_ruby_4237.zip -d /tmp
