#!/usr/bin/env python3
"""get method function"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function returning a tuple"""
    return (page_size*(page-1), page_size*page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int, AssertionError
        assert type(page_size) == int, AssertionError
        assert page > 0, AssertionError
        assert page_size > 0, AssertionError
        assert type(page) == int, AssertionError
        indexes = index_range(page, page_size)
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            data = [row for row in reader]
        return data[indexes[0]+1:indexes[1]+1]
