FROM python:3.10

WORKDIR /app

COPY requirements.tx[t] .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /app/run_challenge
RUN chmod +x /app/run_tests