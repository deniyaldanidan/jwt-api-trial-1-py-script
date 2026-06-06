"""
Module for custom Exceptions
"""


class APIRequestFailedError(Exception):
    """
    Raised When an Request Failed for unknown reason
    """

    def __init__(self, *args):
        super().__init__(*args)


class AlreadyExistError(Exception):
    """
    Raised When an Resource already exist
    """

    def __init__(self, *args):
        super().__init__(*args)


class NotFoundError(Exception):
    """
    Raised When an Resource not found
    """

    def __init__(self, *args):
        super().__init__(*args)
