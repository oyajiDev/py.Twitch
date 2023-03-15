# -*- coding: utf-8 -*-
from dataclasses import dataclass
from .ranges import DateRange
from .pagination import Pagination


@dataclass
class ExtensionAnalyticsItem:
    extension_id:str
    URL:str
    type:str
    date_range:DateRange

    @staticmethod
    def from_data(data:dict):
        return ExtensionAnalyticsItem(
            extension_id = data["extension_id"],
            URL = data["URL"],
            type = data["type"],
            date_range = DateRange.from_data(data["date_range"])
        )

@dataclass
class ExtensionAnalyticsResult:
    data:list
    pagination:Pagination

    @staticmethod
    def from_result(result:dict):
        return ExtensionAnalyticsResult(
            data = [ ExtensionAnalyticsItem.from_data(data) for data in result.pop("data", []) ],
            pagination = Pagination.from_data(result.pop("pagination", { "cursor": "" }))
        )


@dataclass
class GameAnalyticsItem:
    game_id:str
    URL:str
    type:str
    date_range:DateRange

    @staticmethod
    def from_data(data:dict):
        return GameAnalyticsItem(
            game_id = data["game_id"],
            URL = data["URL"],
            type = data["type"],
            date_range = DateRange.from_data(data["date_range"])
        )

@dataclass
class GameAnalyticsResult:
    data:list
    pagination:Pagination

    @staticmethod
    def from_result(result:dict):
        return GameAnalyticsResult(
            data = [ GameAnalyticsItem.from_data(data) for data in result.pop("data", []) ],
            pagination = Pagination.from_data(result.pop("pagination", { "cursor": "" }))
        )
