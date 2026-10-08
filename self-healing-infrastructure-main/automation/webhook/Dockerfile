FROM python:3.12-slim

WORKDIR /webhook

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ansible \
        docker.io \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY webhook.py .

EXPOSE 5001

ENV PYTHONUNBUFFERED=1

CMD ["python", "webhook.py"]
