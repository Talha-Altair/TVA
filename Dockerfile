# Use the LTS release.
FROM python:3.9.4-slim-buster

# RUN useradd --user-group --create-home --shell /bin/false app 

# WORKDIR /home/tact/dockerizing-flask

ADD . /talha

WORKDIR /talha

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python3"]

CMD ["app.py"]

# USER app
