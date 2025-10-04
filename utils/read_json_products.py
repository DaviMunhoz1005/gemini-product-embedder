import json

def get_products_from_json(json_path: str):
    with open(json_path, "r", encoding="utf-8") as file:
        products = json.load(file)
    return products