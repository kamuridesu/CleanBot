FROM python:3.9-slim
RUN pip install aiogram
WORKDIR /app
COPY ./src ./src/
COPY ./main.py .
ENTRYPOINT [ "python", "main.py" ]