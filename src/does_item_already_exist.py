"""
helper functions to check if item already exist in API
"""

import json

ALL_ITEMS_OUT_FILE = "out/allItems.json"


def does_item_with_id_already_exist_and_same_in_json(item):
    """
    Don't forget to update the allItems.json,
    by callng the readAllItems.py before using this function
    """

    with open(ALL_ITEMS_OUT_FILE, "r", encoding="utf-8") as file:
        items: list = json.load(file)
        for i in items:
            if i["id"] == item["id"]:
                new_i = i.copy()
                new_i.update({"category_id": i["category"]["cat_id"]})
                new_i.pop("category")
                # print(new_i)
                # print(item)
                return new_i == item


def does_item_without_id_already_exist_and_same_in_json(item):
    """Don't forget to update the allItems.json,
    by callng the readAllItems.py before using this function"""

    with open(ALL_ITEMS_OUT_FILE, "r", encoding="utf-8") as file:
        items: list = json.load(file)
        for i in items:
            new_i = i.copy()
            new_i.update({"category_id": i["category"]["cat_id"]})
            new_i.pop("category")
            new_i.pop("id")
            # print(new_i)
            # print(item)
            if new_i == item:
                return True
