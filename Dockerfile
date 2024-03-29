FROM python:3.10-slim

WORKDIR /app_menu

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
CMD python ./manage.py migrate && python ./manage.py runserver 0.0.0.0:8000