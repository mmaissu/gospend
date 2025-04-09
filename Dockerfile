FROM python:3.9-slim

WORKDIR /app

COPY gospend_backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/static

CMD ["sh", "-c", "python gospend_backend/manage.py migrate && python gospend_backend/manage.py runserver 0.0.0.0:8000"] 