FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requeriments.txt /app/requeriments.txt
RUN pip install -r requeriments.txt
COPY . /app