FROM  onkar17/keras-tensorflow

RUN   pip3 install flask

RUN   mkdir templates

COPY  dl_model.h5  /

COPY  app.py  /

COPY  templates  /templates 

EXPOSE  1111

ENTRYPOINT  flask run --host=0.0.0.0 --port=1111
