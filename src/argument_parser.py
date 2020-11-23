import argparse


class ArgumentParser:
    def __init__(self):
        argument_parser = argparse.ArgumentParser()
        argument_parser.add_argument(
            "-c", "--crawl", action="store_true", help="crawling mode"
        )
        argument_parser.add_argument(
            "-s", "--scrap", action="store_true", help="scraping mode"
        )
        self.arguments = argument_parser.parse_args()
