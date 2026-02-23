from python:3.11-slim

workdir /app
copy app/requirements.txt .
run pip install -r requirements.txt

copy app/ .

expose 5000
cmd ["python", "app.py"]