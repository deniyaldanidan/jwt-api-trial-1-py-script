"""
Edit An Item module
"""

from requests import Session
from myurls import MY_URLS
from readAllItems import readAllItems
from loginAsAdmin import loginAsAdmin
from does_item_already_exist import does_item_with_id_already_exist_and_same_in_json
from custHeaders import CONTENT_TYPE_JSON_HEADER
import ansiEscapeCodes
from cust_exceptions import APIRequestFailedError

ITEMS_TO_EDIT = [
    {
        "id": 1,
        "name": "Onions",
        "price": 20,
        "description": "fresh onions harvested from an nearby organic farm",
        "item_qty": 250,
        "item_unit": "g",
        "veg": True,
        "category_id": 3,
    },
    {
        "id": 2,
        "name": "Tomatoes",
        "price": 35,
        "description": "fresh tomatoes harvested from an nearby organic farm",
        "item_qty": 500,
        "item_unit": "g",
        "veg": True,
        "category_id": 3,
    },
    {
        "id": 3,
        "name": "Chilli",
        "price": 15,
        "description": "fresh chillies harvested from an nearby organic farm",
        "item_qty": 250,
        "item_unit": "g",
        "veg": True,
        "category_id": 3,
    },
]


def edit_item(s: Session, item):
    """Edit Item Function

    Args:
        s (Session): Session object from LoginAdmin
        item (_type_): Edit Item Data

    Raises:
        Exception: _description_
    """

    r = s.put(MY_URLS.editItem, json=item, headers=CONTENT_TYPE_JSON_HEADER)
    if r.status_code == 200:
        print(
            f"{ansiEscapeCodes.GREEN}Item id: {item["id"]} edited{ansiEscapeCodes.RESET}"
        )
    else:
        print(r.json())
        raise APIRequestFailedError("Unknown error happened")


if __name__ == "__main__":
    readAllItems()
    sess = loginAsAdmin()
    for j in ITEMS_TO_EDIT:
        res = does_item_with_id_already_exist_and_same_in_json(j)
        if not res:
            edit_item(s=sess, item=j)
    readAllItems()
