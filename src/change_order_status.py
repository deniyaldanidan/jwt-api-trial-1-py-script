"""Change Order Status Module"""

from myurls import MY_URLS
from loginAsAdmin import loginAsAdmin
from cust_exceptions import NotFoundError, APIRequestFailedError
from requests import Session
import ansiEscapeCodes
from admin_view_all_orders import admin_view_all_orders

ORDER_ID = "f96d95f8-fec8-4f91-b083-710208a45bd8"
ORDER_STATUS = "confirmed"


def change_order_status(s: Session, order_id: str, order_status: str):
    """Change Order's Status

    Args:
        s (Session): Session from loginAsAdmin
        order_id (str): Order ID
        order_status (str): New Order Status

    Raises:
        NotFoundError: Raised if order not found
        APIRequestFailedError: Raised if Unexpected error happened
    """
    _url = MY_URLS.changeOrderStatus(order_id, order_status)
    print(_url)
    r = s.put(MY_URLS.changeOrderStatus(order_id, order_status))
    # print(r.text)
    if r.status_code == 200:
        print(
            f"{ansiEscapeCodes.GREEN} Order {order_id} status is changed to {order_status}"
        )
    elif r.status_code == 404:
        raise NotFoundError("Requested order not found")
    else:
        raise APIRequestFailedError("Unexpected error happened")


if __name__ == "__main__":
    sess = loginAsAdmin()
    change_order_status(s=sess, order_id=ORDER_ID, order_status=ORDER_STATUS)
    admin_view_all_orders(sess)
