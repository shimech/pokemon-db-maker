import os
import shutil
import time
import requests
from bs4 import BeautifulSoup
from settings import Settings


class Utils:
    @staticmethod
    def make_dir(base_dir, dir_name=""):
        dir_path = os.path.join(base_dir, dir_name)
        if os.path.isdir(dir_path):
            print("PATH: {} はすでに存在します。".format(dir_path))
        else:
            os.makedirs(dir_path)
            print("PATH: {} を作成しました。".format(dir_path))
        return dir_path

    @staticmethod
    def remove_dir(dir_path):
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            print("PATH: {} を削除しました。".format(dir_path))
        else:
            print("PATH: {} は存在しません。".format(dir_path))

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
    def get_html(url, sleep_time=1.5, encoding=Settings.ENCODING):
        response = requests.get(url)
        time.sleep(sleep_time)
        response.encoding = encoding
        bs = BeautifulSoup(response.text, "html.parser")
        return bs

    @staticmethod
    def remove_space_and_nl(string):
        string = string.replace(" ", "")
        string = string.replace("\n", "")
        return string

    @staticmethod
    def is_same_status(i, stat, stat_db):
        for i_comp, stat_comp in enumerate(stat_db):
            if stat == stat_comp and i != i_comp:
                return True
        return False
