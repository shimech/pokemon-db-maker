import sys
from argument_parser import ArgumentParser
from crawler import Crawler
from scraper import Scraper


def main():
    argument_parser = ArgumentParser()
    is_both = not argument_parser.arguments.crawl ^ argument_parser.arguments.scrap

    if is_both:
        Crawler.run()
        Scraper.run()
    else:
        if argument_parser.arguments.crawl:
            Crawler.run()
        elif argument_parser.arguments.scrap:
            Scraper.run()


if __name__ == "__main__":
    main()
