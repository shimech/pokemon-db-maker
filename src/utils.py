import os
from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Utils:
    @staticmethod
    def make_dir(base_dir, dir_name):
        dir_path = os.path.join(base_dir, dir_name)
        if os.path.isdir(dir_path):
            print("PATH: {} はすでに存在します。".format(dir_path))
        else:
            os.makedirs(dir_path)
            print("PATH: {} を作成しました。".format(dir_path))
        return dir_path

    @staticmethod
    def write_html(src_html, base_dir, file_name):
        file_path = os.path.join(base_dir, file_name)
        with open(file_path, mode="w", encoding="utf-8") as f:
            f.write(src_html)
            print("FILE: {} を作成しました。".format(file_path))

    @staticmethod
    def read_html(file_path):
        with open(file_path, mode="r", encoding="utf-8") as f:
            html_str = f.read()
            print("FILE: {} を読み取りました。".format(file_path))
        return html_str

    @staticmethod
    def get_html(url, time=1.5):
        html = urlopen(url).read()
        sleep(time)
        bs = BeautifulSoup(html, "html.parser")
        return bs

    @staticmethod
    def remove_space_and_nl(string):
        string = string.replace(" ", "")
        string = string.replace("\n", "")
        return string
