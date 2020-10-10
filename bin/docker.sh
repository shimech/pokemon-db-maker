#!/bin/sh

docker build -t pokemon-db-maker .
docker run -it --rm -v $PWD:/usr/local/work -w /usr/local/work pokemon-db-maker pipenv run start
