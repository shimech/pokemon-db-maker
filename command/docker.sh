#!/bin/sh

docker build -t pokemon-db-maker .
docker run -it --rm -v $PWD/output:/usr/local/work/output -w /usr/local/work pokemon-db-maker pipenv run start
