#!/bin/sh

docker run -it --rm -v $PWD:/usr/local/app -w /usr/local/app pokemon-db-maker python ./src/convert_csv2json.py
