FROM  onkar17/keras-tensorflow

RUN   pip3 install flask  &&  mkdir templates

COPY  . / 

EXPOSE  1111

ENTRYPOINT  flask run --host=0.0.0.0 --port=1111
