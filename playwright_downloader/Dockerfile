FROM python:3.11-slim

# Установим зависимости для браузеров
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg \
    chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Установка Playwright
RUN pip install --no-cache-dir playwright fastapi uvicorn[standard]
RUN playwright install --with-deps chromium

WORKDIR /app
COPY server.py /app/server.py

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
