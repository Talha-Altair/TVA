FROM python:3.9.4-slim-buster

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]
