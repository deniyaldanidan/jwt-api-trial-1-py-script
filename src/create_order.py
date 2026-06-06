"""Create Order Module"""

from myurls import MY_URLS
import ansiEscapeCodes
from requests import Session
from loginAsUser import signIn
from cust_exceptions import APIRequestFailedError
from add_items_to_cart import add_to_cart

ITEMS_TO_ADD = [
    {"item_id": 11, "count": 2},
    {"item_id": 2, "count": 5},
    {"item_id": 12, "count": 1},
]


def create_order(s: Session):
    """Create Order for the logged-id User

    Args:
        s (Session): Session from loginAsUser

    Raises:
        APIRequestFailedError: Unexpected Error Happened while calling the API
    """
    r = s.post(MY_URLS.makeOrder)
    if r.status_code == 201:
        print(f"{ansiEscapeCodes.GREEN} order is created {ansiEscapeCodes.RESET}")
    else:
        print(r.json())
        raise APIRequestFailedError("Unknown error happened")


if __name__ == "__main__":
    sess = signIn()
    for itm in ITEMS_TO_ADD:
        add_to_cart(sess, itm)
    create_order(sess)
