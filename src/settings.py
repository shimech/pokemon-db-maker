class Settings:
    BASE_URL = "https://yakkun.com/swsh/"
    STATUS_LIST_URL = BASE_URL + "stats_list.htm?mode=all"

    STATUS = {
        "HP": "hitpoint",
        "こうげき": "attack",
        "ぼうぎょ": "block",
        "とくこう": "contact",
        "とくぼう": "defense",
        "すばやさ": "speed",
        "合計": "total"
    }

    REGIONS = {
        1: "カントー",
        2: "ジョウト",
        3: "ホウエン",
        4: "シンオウ",
        5: "イッシュ",
        6: "カロス",
        7: "アローラ",
        8: "ガラル",
    }

    COLUMNS = [
        "No.",
        "なまえ",
        "タイプ1",
        "タイプ2",
        "とくせい1",
        "とくせい2",
        "ゆめとくせい",
        "HP",
        "こうげき",
        "ぼうぎょ",
        "とくこう",
        "とくぼう",
        "すばやさ",
        "合計",
        "最終進化",
        "地方",
    ]
