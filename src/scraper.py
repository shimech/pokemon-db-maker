import os
import re
import pandas as pd
from glob import glob
from bs4 import BeautifulSoup
from settings import Settings
from utils import Utils
from pokemon import Pokemon


class Scraper:
    FILE_PATH = os.path.abspath(__file__)

    @classmethod
    def run(cls):
        print("### スクレイピング開始 ###")

        pokemon_df = cls.__init_pokemon_df(Settings.COLUMNS)
        detail_page_html_paths = sorted(glob(os.path.join(os.path.dirname(
            os.path.dirname(cls.FILE_PATH)), "html/detail_page/*.html")))
        for detail_page_html_path in detail_page_html_paths:
            pokemon = Pokemon()
            html_str = Utils.read_html(detail_page_html_path)
            detail_page_bs = BeautifulSoup(html_str, "html.parser")

            pokemon.no, pokemon.name = re.match(
                r".*/([0-9]{3})_(.+).html", detail_page_html_path).groups()
            pokemon.types = cls.__get_types(detail_page_bs)
            pokemon.abilities = cls.__get_abilities(detail_page_bs)
            pokemon.status = cls.__get_status(detail_page_bs)
            pokemon.is_final = cls.__get_is_final(detail_page_bs)
            pokemon.region = cls.__get_region(pokemon.no, pokemon.name)

            print(pokemon)

            pokemon_srs = pd.Series(
                data=pokemon.reshape_to_list(), index=Settings.COLUMNS)
            pokemon_df = pokemon_df.append(pokemon_srs, ignore_index=True)

        csv_path = Utils.make_dir(os.path.dirname(
            os.path.dirname(cls.FILE_PATH)), "output")
        pokemon_df.to_csv(os.path.join(csv_path, "pokemon_db.csv"),
                          index=False, encoding="utf-8")
        print("FILE: {} を出力しました。".format(
            os.path.join(csv_path, "pokemon_db.csv")))

        print("### スクレイピング終了 ###")

    @staticmethod
    def __init_pokemon_df(columns):
        return pd.DataFrame(columns=columns)

    @staticmethod
    def __get_types(bs):
        type_ul_bs = bs.find("ul", {"class": "type"})
        type_imgs_bs = type_ul_bs.find_all("img")
        if len(type_imgs_bs) == 1:
            type_imgs_bs.append(None)

        types = []
        for type_img_bs in type_imgs_bs:
            if type_img_bs is None:
                types.append("")
            else:
                types.append(type_img_bs.get("alt"))

        return types

    @staticmethod
    def __get_abilities(bs):
        detail_data_bs = bs.find("table", {"summary": "詳細データ"})
        detail_data_trs_bs = detail_data_bs.find_all("tr")

        mode = None
        abilities = {
            "normal": [],
        }
        for detail_data_tr_bs in detail_data_trs_bs:
            if detail_data_tr_bs.find("th") is None:
                if mode is None:
                    pass
                elif mode == "normal":
                    normal_ability = detail_data_tr_bs.find("a").text
                    abilities[mode].append(
                        Utils.remove_space_and_nl(normal_ability))
                elif mode == "special":
                    special_ability = detail_data_tr_bs.find("td").text
                    special_ability = Utils.remove_space_and_nl(
                        special_ability)
                    abilities[mode] = special_ability[1:] if special_ability != "なし" else ""

            else:
                if "特性(とくせい)" in detail_data_tr_bs.find("th").text:
                    mode = "normal"
                elif "隠れ特性(夢特性)" in detail_data_tr_bs.find("th").text:
                    mode = "special"
                else:
                    mode = None

        if len(abilities["normal"]) == 1:
            abilities["normal"].append("")

        return abilities

    @staticmethod
    def __get_status(bs):
        detail_data_bs = bs.find("table", {"summary": "詳細データ"})
        detail_data_trs_bs = detail_data_bs.find_all("tr")

        is_status_column = False
        status = {}
        for detail_data_tr_bs in detail_data_trs_bs:
            if detail_data_tr_bs.find("th") is None:
                if is_status_column:
                    detail_data_tds_bs = detail_data_tr_bs.find_all("td")

                    label = Utils.remove_space_and_nl(
                        detail_data_tds_bs[0].text)
                    key = Settings.STATUS.get(label)

                    if key is not None:
                        value_str = Utils.remove_space_and_nl(
                            detail_data_tds_bs[1].text)
                        value = int(re.search(r"\d+", value_str).group())
                        status[key] = value

            else:
                is_status_column = ("種族値" in detail_data_tr_bs.find("th").text)

        status["total"] = sum(status.values())

        return status

    @staticmethod
    def __get_is_final(bs):
        simple_name = Utils.remove_space_and_nl(
            bs.find("tr", {"class": "head"}).find("th").text)

        evo_list_bs = bs.find("ul", {"class": "evo_list"})

        if evo_list_bs is None:
            return True

        evo_lis_bs = evo_list_bs.find_all("li")
        is_check = False
        for evo_li_bs in reversed(evo_lis_bs):
            if evo_li_bs.get("class") is not None and "evo_arrow" in evo_li_bs.get("class"):
                is_check = True

            else:
                if is_check:
                    is_check = False

                    a_bs = evo_li_bs.find("a")
                    if a_bs is not None:
                        compare_name = Utils.remove_space_and_nl(a_bs.text)
                        if simple_name == compare_name:
                            return False

        return True

    @staticmethod
    def __get_region(no, name):
        no = int(no)

        if "アローラ" in name:
            return 7
        elif "ガラル" in name:
            return 8

        if no <= 151:
            return 1
        elif 151 < no <= 251:
            return 2
        elif 251 < no <= 386:
            return 3
        elif 386 < no <= 494:
            return 4
        elif 494 < no <= 649:
            return 5
        elif 649 < no <= 721:
            return 6
        elif 721 < no <= 809:
            return 7
        elif 809 < no:
            return 8
