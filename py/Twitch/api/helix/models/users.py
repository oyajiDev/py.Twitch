# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import datetime
from typing import List
from .pagination import Pagination


@dataclass
class UserItem:
    id:str
    login:str
    display_name:str
    type:str
    broadcaster_type:str
    description:str
    profile_image_url:str
    offline_image_url:str
    # view_count:int # deprecated: https://discuss.dev.twitch.tv/t/get-users-api-endpoint-view-count-deprecation/37777
    email:str
    created_at:datetime

    @staticmethod
    def from_data(data:dict):
        return UserItem(
            id = data["id"],
            login = data["login"],
            display_name = data["display_name"],
            type = data["type"],
            broadcaster_type = data["broadcaster_type"],
            description = data["description"],
            profile_image_url = data["profile_image_url"],
            offline_image_url = data["offline_image_url"],
            email = data.pop("email", ""),
            created_at = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        )


@dataclass
class BannedUserItem:
    user_id:str
    user_login:str
    user_name:str
    expires_at:datetime
    created_at:datetime
    reason:str
    moderator_id:str
    moderator_login:str
    moderator_name:str

    @staticmethod
    def from_data(data:dict):
        return BannedUserItem(
            user_id = data["user_id"],
            user_login = data["user_login"],
            user_name = data["user_name"],
            expires_at = datetime.strptime(data["expires_at"], "%Y-%m-%dT%H:%M:%SZ"),
            created_at = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
            reason = data["reason"],
            moderator_id = data["moderator_id"],
            moderator_login = data["moderator_login"],
            moderator_name = data["moderator_name"]
        )

@dataclass
class BannedUserResult:
    data:List[BannedUserItem]
    pagination:Pagination

    @staticmethod
    def from_result(result:dict):
        return BannedUserResult(
            data = [ BannedUserItem.from_data(data) for data in result.pop("data", []) ],
            pagination = Pagination.from_data(result.pop("pagination", { "cursor": "" }))
        )
