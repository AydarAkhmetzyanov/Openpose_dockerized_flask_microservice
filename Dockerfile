FROM python:3


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN apt-get update && apt-get install -y vim git

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade cython
RUN pip install numpy

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
