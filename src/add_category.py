"""
Add Category to the API Module
"""

from requests import Session
from loginAsAdmin import loginAsAdmin
from myurls import MY_URLS
from readAllCategories import readAllCategories
from custHeaders import CONTENT_TYPE_JSON_HEADER
from cust_exceptions import AlreadyExistError, APIRequestFailedError

category_data = {"name": "rice"}


def add_category(s: Session):
    """Add Category Function

    Args:
        s (Session): Session object from LoginAdmin

    Raises:
        Exception: _description_

    """
    r = s.post(
        MY_URLS.createCategory, json=category_data, headers=CONTENT_TYPE_JSON_HEADER
    )
    # print(s.cookies.get("refresh"))
    if r.status_code == 409:
        raise AlreadyExistError("Category already exist")
    if r.status_code == 201:
        readAllCategories()
    else:
        raise APIRequestFailedError("Unknown error happened")


if __name__ == "__main__":
    sess = loginAsAdmin()
    add_category(sess)
