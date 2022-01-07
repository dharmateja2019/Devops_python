FROM python:3.10.0a4-buster
COPY . /app
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
CMD ["python", "app.py"]
