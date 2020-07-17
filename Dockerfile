FROM python:3.7
WORKDIR /usr/tryouts
COPY . /usr/tryouts
RUN pip -m install --no-cache-dir setup.py
