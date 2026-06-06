"""Add Items to Cart Module"""

from myurls import MY_URLS
from cust_exceptions import APIRequestFailedError, NotFoundError
from requests import Session
from custHeaders import CONTENT_TYPE_JSON_HEADER
import ansiEscapeCodes


def add_to_cart(s: Session, cart_data):
    """Add To Cart

    Args:
        s (Session): session from loginAsUser
        cart_data (_type_): Cart Item Data

    Raises:
        NotFoundError: Requested Item not found
        APIRequestFailedError: Unknown Error happened
    """
    r = s.post(MY_URLS.addToCart, json=cart_data, headers=CONTENT_TYPE_JSON_HEADER)
    if r.status_code == 201:
        print(f"{ansiEscapeCodes.GREEN} Item {cart_data["item_id"]} is added to cart")
    elif r.status_code == 404:
        raise NotFoundError("Requested resource not found")
    else:
        print(r.json())
        raise APIRequestFailedError("Unknown error happened")
