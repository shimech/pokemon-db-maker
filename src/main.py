from argument_parser import ArgumentParser
from crawler import Crawler
from scraper import Scraper


def main():
    argument_parser = ArgumentParser()
    # どちらも指定されてない or どちらも指定されている場合にどちらも行う
    is_both = not argument_parser.arguments.crawl ^ argument_parser.arguments.scrape

    if is_both:
        Crawler.run()
        Scraper.run()
    else:
        if argument_parser.arguments.crawl:
            Crawler.run()
        elif argument_parser.arguments.scrape:
            Scraper.run()


if __name__ == "__main__":
    main()
