install:
	poetry install

build:
	sh ./bin/build.sh

docker-run:
	sh ./bin/run/sh

docker-crawl:
	sh ./bin/crawl.sh

docker-scrape:
	sh ./bin/scrape.sh

local-run:
	poetry run python ./src/main.py

local-crawl:
	poetry run python ./src/main.py --crawl

local-scrape:
	poetry run python ./src/main.py --scrape
