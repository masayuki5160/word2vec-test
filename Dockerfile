FROM python:3.6

# VOLUME /home/irisdata-chainer

RUN apt-get update && \
    apt-get -y install sudo vim unzip && \
    pip install --upgrade gensim && \
    pip install janome && \
    cd /home/ && \
    wget http://www.aozora.gr.jp/cards/000148/files/794_ruby_4237.zip && \
    unzip 794_ruby_4237.zip
