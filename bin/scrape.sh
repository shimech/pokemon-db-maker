#!/bin/sh

docker run -it --rm -v $PWD:/usr/local/app -w /usr/local/app pokemon-db-maker python ./src/main.py --scrape
