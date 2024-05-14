FROM python:3.11

RUN apt-get update && apt-get install -y ffmpeg

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ["python", "main.py"]