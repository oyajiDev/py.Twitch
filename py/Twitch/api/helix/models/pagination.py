# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Pagination:
    cursor:str

    @staticmethod
    def from_data(data:dict):
        return Pagination(
            cursor = data.pop("cursor", "")
        )
