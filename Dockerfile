FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y firefox-esr

RUN apt-get update && apt-get install -y \
    default-jre-headless \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.zip \
    && unzip allure-2.24.0.zip -d /opt/ \
    && ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure \
    && rm allure-2.24.0.zip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD pytest --alluredir=allure-results && allure generate allure-results -o allure-report --clean