#!/bin/sh

docker run -it --rm -v $PWD:/usr/local/work -w /usr/local/work pokemon-db-maker pipenv run python ./src/convert_csv_to_json.py
