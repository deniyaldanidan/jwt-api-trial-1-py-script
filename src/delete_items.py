"""Delete Items Module"""

from myurls import MY_URLS
from loginAsAdmin import loginAsAdmin
from readAllItems import readAllItems
import ansiEscapeCodes
from requests import Session
from cust_exceptions import APIRequestFailedError

ITEMS_TO_DELETE = [6, 7, 8, 9, 10]


def delete_items(s: Session, item_id: int):
    """delete Items from API

    Args:
        s (Session): session from loginAdmin
        item_id (int): Item Id

    Raises:
        APIRequestFailedError: Request failed for unknown reasons
    """
    r = s.delete(MY_URLS.deleteItem(item_id))
    if r.status_code == 200:
        print(f"{ansiEscapeCodes.GREEN} Item {item_id} deleted {ansiEscapeCodes.RESET}")
    else:
        raise APIRequestFailedError("Unknown error happened")


if __name__ == "__main__":
    sess = loginAsAdmin()
    for i in ITEMS_TO_DELETE:
        delete_items(s=sess, item_id=i)
    readAllItems()
