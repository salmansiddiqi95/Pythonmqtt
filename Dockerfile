FROM python:3.8-slim-buster

RUN python3 -m pip install paho-mqtt
COPY . /
CMD ["python3", "app.py"]