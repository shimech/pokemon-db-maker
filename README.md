# ポケモン図鑑メーカー

## Dependencies

- local OS: macOS Big Sur 11.2.3
- Python: 3.9.4
- Poetry: 1.1.4
- Docker: 20.10.5

## Usage

### install packages

```sh
make install
```

### build an environment on docker

```sh
make build
```

### run both of crawler and scraper

on docker

```sh
make docker-run
```

on local

```sh
make local-run
```

only crawler

```sh
make docker-run --crawl
```

only scraper

```sh
make docker-run --scrape
```

### convert csv to json

on docker

```sh
make docker-csv2json
```

on local

```sh
make local-csv2json
```

## Reference

- [ポケモン徹底攻略](https://yakkun.com/swsh/stats_list.htm?mode=all)
