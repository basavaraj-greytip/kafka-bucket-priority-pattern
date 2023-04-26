FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip &&  \
    pip install --no-cache-dir --user -r requirements.txt

ENTRYPOINT ["python", "-m", "main"]
