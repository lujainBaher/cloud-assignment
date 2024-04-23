FROM python:latest

WORKDIR /DockerFiles

COPY random_paragraphs.txt main.py ./

RUN pip install nltk

ENTRYPOINT ["python", "main.py"] 
