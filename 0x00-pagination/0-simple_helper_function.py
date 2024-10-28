#!/usr/bin/env python3
""" This returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return
    in a list for exact pagination parameters.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This returns a tuple containing start index and end index
        corresponding to the range of indexes to ruturn
        in a list.
    """
    return ((page - 1) * page_size, page * page_size)
