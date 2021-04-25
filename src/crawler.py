import os
from settings import Settings
from utils import Utils


class Crawler:
    FILE_PATH = os.path.abspath(__file__)

    @classmethod
    def run(cls):
        print("### クローリング開始 ###")

        html_dir_path = os.path.join(os.path.dirname(
            os.path.dirname(cls.FILE_PATH)), "html")
        Utils.remove_dir(html_dir_path)
        Utils.make_dir(html_dir_path)

        status_list_page_dir_path = Utils.make_dir(
            html_dir_path, "status_list_page")
        status_list_bs = Utils.get_html(Settings.STATUS_LIST_URL)
        Utils.write_html(status_list_bs.prettify(),
                         status_list_page_dir_path, "status_list.html")

        detail_page_dir_path = Utils.make_dir(html_dir_path, "detail_page")
        status_table_bs = status_list_bs.find(
            "table", {"class": "center stupidtable stupidtable_common"})
        trs = status_table_bs.find_all("tr")
        for tr in trs[1:]:  # 1番目の要素はカラム名であるためスキップ
            a = tr.find("a")

            detail_page_url = Settings.BASE_URL + a["href"]
            detail_page_bs = Utils.get_html(detail_page_url)

            no = tr.find("td", {"class": "c1"}).text
            file_name = "{}_{}.html".format(no, a.text)
            if a.text in Settings.EXCEPT_POKEMON_NAMES:
                print("{} は除外されました。".format(a.text))
            else:
                Utils.write_html(detail_page_bs.prettify(),
                                 detail_page_dir_path, file_name)

        print("### クローリング終了 ###")
