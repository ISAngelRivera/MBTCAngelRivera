FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN [ ! -d "logs" ] || mkdir -p logs

EXPOSE 5000

CMD ["python", "theforceapp.py"]

