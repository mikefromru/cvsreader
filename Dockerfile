FROM python:3.11-alpine

# set work directory
WORKDIR /project


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip3 install --upgrade pip 
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY /entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]

# copy project
COPY . /project

