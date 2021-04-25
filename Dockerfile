FROM python:3.9.4

ARG work_dir=/usr/local/work/

ADD . $work_dir

WORKDIR $work_dir

RUN export LANG=C.UTF-8 && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install
