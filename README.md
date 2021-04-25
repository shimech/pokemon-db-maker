# ポケモン図鑑メーカー

## Dependencies

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

## Reference

- [ポケモン徹底攻略](https://yakkun.com/swsh/stats_list.htm?mode=all)
