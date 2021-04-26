FROM python:3.8.8 
#nikolaik/python-nodejs:latest
#

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

#port
EXPOSE 6000

#run gnicorn
CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:6000", "app:create_app()"]
