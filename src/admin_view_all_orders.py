"""View All Orders for Admin Module"""

from requests import Session
from myurls import MY_URLS
from writeResponseIntoJsonFile import handleResponse
from cust_exceptions import APIRequestFailedError
from loginAsAdmin import loginAsAdmin

OUT_FILENAME = "out/adminAllOrders.json"


def admin_view_all_orders(s: Session):
    """admin view all orders

    Args:
        s (Session): Session from loginInAdmin

    Raises:
        APIRequestFailedError: Unexpected Error Happened
    """
    r = s.get(MY_URLS.adminViewAllOrders)
    if r.status_code == 200:
        handleResponse(r.json(), OUT_FILENAME, MY_URLS.adminViewAllOrders)
    else:
        raise APIRequestFailedError


if __name__ == "__main__":
    sess = loginAsAdmin()
    admin_view_all_orders(sess)
