FROM python:3.13.0-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./src/

EXPOSE 5000

CMD ["python", "./src/main.py"]
