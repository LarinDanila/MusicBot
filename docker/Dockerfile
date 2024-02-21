FROM python:3.10
ENV PYTHONPATH "${PYTHONPATH}:/MusicBot/app"
WORKDIR /MusicBot
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
COPY ../requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY ../. .
CMD ["python", "app/main.py"]