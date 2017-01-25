FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD . /src/
RUN pip install -r src/requirements/requirements.txt
RUN pip install -r src/requirements/modules.txt
