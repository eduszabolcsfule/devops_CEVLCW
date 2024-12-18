FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "main.py"]

