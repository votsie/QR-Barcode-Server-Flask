# Используем официальный Python образ
# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
# Set the working directory inside the container
WORKDIR /app

# Копируем все файлы из текущей директории на хосте в контейнер
# Copy all files from the current directory on the host machine to the container
COPY . /app

# Устанавливаем зависимости
# Install the dependencies listed in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 5000 для связи с Flask
# Expose port 5000 to allow communication with Flask
EXPOSE 5000

# Запускаем приложение
# Run the application
CMD ["python", "app.py"]

