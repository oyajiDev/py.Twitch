# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List
from datetime import datetime
from .pagination import Pagination


@dataclass
class StreamItem:
    id:str
    user_id:str
    user_login:str
    user_name:str
    game_id:str
    game_name:str
    type:str
    title:str
    tags:List[str]
    viewer_count:int
    started_at:datetime
    language:str
    thumbnail_url:str
    tag_ids:List[str]
    is_mature:bool

    @staticmethod
    def from_data(data:dict):
        return StreamItem(
            id = data["id"],
            user_id = data["user_id"],
            user_login = data["user_login"],
            user_name = data["user_name"],
            game_id = data["game_id"],
            game_name = data["game_name"],
            type = data["type"],
            title = data["title"],
            tags = data["tags"],
            viewer_count = data["viewer_count"],
            started_at = datetime.strptime(data["started_at"], "%Y-%m-%dT%H:%M:%SZ"),
            language = data["language"],
            thumbnail_url = data["thumbnail_url"],
            tag_ids = data["tag_ids"],
            is_mature = data["is_mature"]
        )

@dataclass
class StreamsResult:
    data:List[StreamItem]
    pagination:Pagination

    @staticmethod
    def from_result(result:dict):
        return StreamsResult(
            data = [ StreamItem.from_data(data) for data in result.pop("data", []) ],
            pagination = Pagination.from_data(result.pop("pagination", {}))
        )
