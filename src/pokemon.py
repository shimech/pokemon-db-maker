from settings import Settings


class Pokemon:
    def __init__(self, no=None, name=None, types=None, abilities=None, status=None, is_final=None, region=None, is_mega_evolution=None, is_same_status=None):
        if types is None:
            types = [None, None]

        if abilities is None:
            abilities = {
                "normal": [None, None],
                "special": None
            }

        if status is None:
            status = {
                "hitpoint": None,
                "attack": None,
                "block": None,
                "contact": None,
                "defense": None,
                "speed": None,
                "total": None
            }

        self.no = no
        self.name = name
        self.types = types
        self.abilities = abilities
        self.status = status
        self.is_final = is_final
        self.region = region
        self.is_mega_evolution = is_mega_evolution
        self.is_same_status = is_same_status

    def __str__(self):
        return """
               図鑑No.   : {}
               なまえ    : {}
               タイプ    : {}, {}
               とくせい  : {}, {} | {}
               種族値    : H:{} A:{} B:{} C:{} D:{} S:{} | TOTAL:{}
               最終進化  : {}
               地方      : {}
               メガシンカ: {}
               """.format(
            self.no,
            self.name,
            self.types[0], self.types[1],
            self.abilities["normal"][0], self.abilities["normal"][1], self.abilities["special"],
            self.status["hitpoint"], self.status["attack"], self.status["block"], self.status[
                "contact"], self.status["defense"], self.status["speed"], self.status["total"],
            self.is_final,
            Settings.REGIONS.get(self.region),
            self.is_mega_evolution
        )

    def reshape_to_list(self):
        return [
            self.no,
            self.name,
            self.types[0],
            self.types[1],
            self.abilities["normal"][0],
            self.abilities["normal"][1],
            self.abilities["special"],
            self.status["hitpoint"],
            self.status["attack"],
            self.status["block"],
            self.status["contact"],
            self.status["defense"],
            self.status["speed"],
            self.status["total"],
            self.is_final,
            Settings.REGIONS.get(self.region),
            self.is_mega_evolution,
            self.is_same_status
        ]
