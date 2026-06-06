"""Create New Item Module"""

from myurls import MY_URLS
from loginAsAdmin import loginAsAdmin
import ansiEscapeCodes
from requests import Session
from cust_exceptions import APIRequestFailedError, NotFoundError
from custHeaders import CONTENT_TYPE_JSON_HEADER
from does_item_already_exist import does_item_without_id_already_exist_and_same_in_json
from readAllItems import readAllItems

ITEMS_TO_CREATE = [
    {
        "name": "Mozarella",
        "price": 125,
        "description": "Mozarella Cheese made from our own organic factory in nearby village",
        "item_qty": 250,
        "item_unit": "g",
        "veg": False,
        "category_id": 4,
    },
    {
        "name": "Premium Basmati",
        "price": 950,
        "description": "Grown and Harvested from Punjab",
        "item_qty": 10,
        "item_unit": "kg",
        "veg": True,
        "category_id": 6,
    },
]


def create_item(s: Session, item):
    """Create new Item in the API

    Args:
        s (Session): Admin Session object
        item (_type_): New Item

    Raises:
        NotFoundError: Usually raised when an Category_ID not exists
        APIRequestFailedError: When API_REQUEST Failed bcuz of some unknown reason
    """
    r = s.post(MY_URLS.createItem, json=item, headers=CONTENT_TYPE_JSON_HEADER)
    if r.status_code == 201:
        print(
            f"{ansiEscapeCodes.GREEN} Item {item["name"]} successfully created{ansiEscapeCodes.RESET}"
        )
    elif r.status_code == 404:
        raise NotFoundError("Requested resource not found")
    else:
        print(r.json())
        raise APIRequestFailedError("Create Item request failed")


if __name__ == "__main__":
    readAllItems()
    sess = loginAsAdmin()
    for j in ITEMS_TO_CREATE:
        is_exist = does_item_without_id_already_exist_and_same_in_json(j)
        if not is_exist:
            create_item(sess, j)
    readAllItems()
