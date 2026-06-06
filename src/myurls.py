"""
URLS for API values
"""

from typing import NamedTuple, Callable

# from types import SimpleNamespace

# MY_URLS = SimpleNamespace(
#     allItems= "http://localhost:3500/item/view/all",
#     allCategories= "http://localhost:3500/item-category/view/all",
#     createCategory= "http://localhost:3500/item-category/add",
#     logIn= "http://localhost:3500/auth/sign-in",
#     signUp= "http://localhost:3500/auth/sign-up",
#     refresh= "http://localhost:3500/auth/refresh",
#     viewItem= lambda id: f"http://localhost:3500/item/view/{id}"
# )


class URLSCHEMA(NamedTuple):
    """Just an Typing Class for the URL's Object"""

    allItems: str
    allCategories: str
    createCategory: str
    logIn: str
    signUp: str
    refresh: str
    viewItem: Callable[[int], str]
    viewCategory: Callable[[int], str]
    deleteUser: str
    editItem: str
    createItem: str
    deleteItem: Callable[[int], str]
    addToCart: str
    makeOrder: str
    adminViewAllOrders: str
    changeOrderStatus: Callable[[str, str], str]


MY_URLS = URLSCHEMA(
    allItems="http://localhost:3500/item/view/all",
    allCategories="http://localhost:3500/item-category/view/all",
    createCategory="http://localhost:3500/item-category/add",
    logIn="http://localhost:3500/auth/sign-in",
    signUp="http://localhost:3500/auth/sign-up",
    refresh="http://localhost:3500/auth/refresh",
    viewItem=lambda id: f"http://localhost:3500/item/view/{id}",
    viewCategory=lambda id: f"http://localhost:3500/item/view/category/{id}",
    deleteUser="http://localhost:3500/user/delete-me",
    editItem="http://localhost:3500/item/edit",
    createItem="http://localhost:3500/item/create",
    deleteItem=lambda id: f"http://localhost:3500/item/delete/{id}",
    addToCart="http://localhost:3500/cart/add",
    makeOrder="http://localhost:3500/order/create",
    adminViewAllOrders="http://localhost:3500/admin/order/view/all",
    changeOrderStatus=lambda id, status: f"http://localhost:3500/admin/order/change-status/{id}/{status}",
)
