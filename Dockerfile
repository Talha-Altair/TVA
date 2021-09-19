FROM python:3.9.4-slim-buster

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

RUN python -m spacy download en_core_web_sm

RUN python business.py

EXPOSE 5000

ADD . /app

WORKDIR /app

ENTRYPOINT ["python3"]

CMD ["app.py"]
