#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function returning a tuple"""
    return (page_size*(page-1), page_size*page)
