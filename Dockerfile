# Какой язык программирования
FROM python:latest
# Назначить основную нашу папку для Dockerfile
WORKDIR /pythontodo
# Копируем наш проект внутри Dockerfile
COPY . /pythontodo
# Установка библиотек
RUN pip install -r requirements.txt
# Запуск проекта
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=2626"]