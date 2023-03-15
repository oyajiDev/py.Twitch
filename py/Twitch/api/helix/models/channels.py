# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import datetime
from typing import List
from .pagination import Pagination


@dataclass
class FollowedChannelItem:
    broadcaster_id:str
    broadcaster_login:str
    broadcaster_name:str
    followed_at:datetime

    @staticmethod
    def from_data(data:dict):
        return FollowedChannelItem(
            broadcaster_id = data["broadcaster_id"],
            broadcaster_login = data["broadcaster_login"],
            broadcaster_name = data["broadcaster_name"],
            followed_at = datetime.strptime(data["followed_at"], "%Y-%m-%dT%H:%M:%SZ")
        )

@dataclass
class FollowedChannelsResult:
    data:List[FollowedChannelItem]
    pagination:Pagination
    total:int

    @staticmethod
    def from_result(result:dict):
        return FollowedChannelsResult(
            data = [ FollowedChannelItem.from_data(data) for data in result.pop("data", []) ],
            pagination = Pagination.from_data(result.pop("pagination", { "cursor": "" })),
            total = result.pop("total", 0)
        )
