FROM python:3.9.4 AS builder

ARG work_dir=/usr/local/app

WORKDIR $work_dir

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt


FROM python:3.9.4

WORKDIR $work_dir

COPY --from=builder /usr/local/app/requirements.txt .

RUN pip install -r requirements.txt

COPY . .
