FROM python:3.11-buster
RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU.UTF-8
WORKDIR /app
RUN pip3 install pip-tools
COPY pyproject.toml pyproject.toml
RUN pip-compile
RUN pip3 install -r requirements.txt
COPY . .
RUN pip3 install -e .