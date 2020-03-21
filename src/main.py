import sys
from crawler import Crawler
from scraper import Scraper


def main():
    option = sys.argv[1] if len(sys.argv) >= 2 else None
    if option == "--crawl":
        Crawler.run()
    elif option == "--scrap":
        Scraper.run()
    else:
        Crawler.run()
        Scraper.run()


if __name__ == "__main__":
    main()
