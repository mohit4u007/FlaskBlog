FROM python:3.13-slim

RUN mkdir /app
WORKDIR /app

# Set environment variables to optimize the Python runtime
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY run.py .
COPY ./requirements.txt .
COPY create_db_n_fill_dummy_data.py .
COPY posts.json .

RUN pip install --upgrade pip && \
	pip install --no-cache-dir -r requirements.txt

COPY ./flaskblog ./flaskblog

COPY ./entrypoint.sh .
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]