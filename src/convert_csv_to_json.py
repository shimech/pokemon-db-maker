import os
import json
import pandas as pd


OUTPUT_DIR_PATH = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), "output")
CSV_PATH = os.path.join(OUTPUT_DIR_PATH, "pokemon_db.csv")

COLUMNS = {
    "No.": "id",
    "なまえ": "name",
    "タイプ1": "type1",
    "タイプ2": "type2",
    "とくせい1": "normal_ability1",
    "とくせい2": "normal_ability2",
    "ゆめとくせい": "special_ability",
    "HP": "hitpoint",
    "こうげき": "attack",
    "ぼうぎょ": "block",
    "とくこう": "contact",
    "とくぼう": "defense",
    "すばやさ": "speed",
    "合計": "total",
    "最終進化": "is_final",
    "地方": "region",
    "メガシンカ": "is_mega_evolution",
    "同一種族値": "is_same_status"
}


def main():
    pokemon_df = pd.read_csv(CSV_PATH, encoding="utf-8")
    pokemon_df = pokemon_df.rename(columns=COLUMNS)
    pokemon_df = pokemon_df.fillna("")

    pokemon_dicts = []
    for index, row in pokemon_df.iterrows():
        pokemon_dict = {
            "id": index,
            "no": row["id"],
            "name": row["name"],
            "type": [row["type1"], row["type2"]],
            "ability": {
                "normal": [row["normal_ability1"], row["normal_ability2"]],
                "special": row["special_ability"]
            },
            "status": {
                "hitpoint": row["hitpoint"],
                "attack": row["attack"],
                "block": row["block"],
                "contact": row["contact"],
                "defense": row["defense"],
                "speed": row["speed"],
                "total": row["total"]
            },
            "isFinal": row["is_final"],
            "region": row["region"],
            "isMegaEvolution": row["is_mega_evolution"],
            "isSameStatus": row["is_same_status"]
        }
        pokemon_dicts.append(pokemon_dict)

    json_path = os.path.join(OUTPUT_DIR_PATH, "pokemon_db.json")
    with open(json_path, mode="w") as f:
        json.dump(pokemon_dicts, f, ensure_ascii=False, indent=2)

    print("JSON: {} を出力しました。".format(json_path))


if __name__ == "__main__":
    main()
