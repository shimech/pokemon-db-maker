#!/bin/sh

docker run -it --rm -v $PWD:/usr/local/work -w /usr/local/work pokemon-db-maker poetry run python ./src/main.py
