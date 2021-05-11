FROM python:3
MAINTAINER Andrey Varfolomeev
ENV PYTHONUNBUFFERED 1
RUN mkdir /amigo
WORKDIR /amigo
COPY requirements.txt /amigo/
RUN pip install -r requirements.txt
COPY . /amigo/

CMD ["sh", "start.sh"]