# Використовуємо базовий образ Python
FROM python:3.11

# Встановлюємо необхідні пакети
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Копіюємо файли проекту в робочу директорію контейнера
WORKDIR /app
COPY . /app

# Встановлюємо залежності проекту
RUN pip install -r requirements.txt

# Виконуємо команди для тестування
CMD ["pytest", "tests/"]
