# -*- coding: utf-8 -*-
import requests
from typing import Optional, Union, List
from .base import RequestBase
from .._config import base_url
from ..models.users import UserItem, BannedUserResult
from ..errors import MissingScopeError


class UserRequest(RequestBase):
    def __init__(self, app_id:str, user_token:str):
        super().__init__(app_id, user_token)

    def get_user(self, id:Optional[str] = None, login:Optional[str] = None) -> Union[UserItem, None]:
        """
        """
        if id is None and login is None:
            raise RuntimeError("Either `id` or `login` must be specified!")
        elif id is not None:
            users = self.get_users(id = [id])
            if len(users) == 0:
                return None
            else:
                return users[0]
        elif login is not None:
            users = self.get_users(login = [login])
            if len(users) == 0:
                return None
            else:
                return users[0]

    def get_users(self, id:Optional[List[str]] = None, login:Optional[List[str]] = None) -> List[UserItem]:
        url = f"{base_url}/users"
        if id:
            id_to_url = "&id=".join(id)
            url += f"?id={id_to_url}"
        if login:
            login_to_url = "&login=".join(login)
            if url.endswith("/users"):
                url += f"?login={login_to_url}"
            else:
                url += f"&login={login_to_url}"
        
        resp = requests.get(url, headers = self.request_header).json()
        return [
            UserItem.from_data(data)
            for data in resp.pop("data", [])
        ]

    def get_banned_users(self, broadcaster_id:str, user_id:Optional[List[str]] = None, first:Optional[int] = 20, after:Optional[str] = None, before:Optional[str] = None) -> BannedUserResult:
        params = { "broadcaster_id": broadcaster_id }
        if user_id:
            params["user_id"] = user_id
        if first:
            params["first"] = first
        if after:
            params["after"] = after
        if before:
            params["before"] = before
        
        resp = requests.get(f"{base_url}/moderation/banned", params = params, headers = self.request_header).json()
        if "error" in resp.keys() and resp["message"].startswith("Missing scope:"):
            raise MissingScopeError("At least one scope is required: modulation:read or modifier:manage:banned_users!")

        return BannedUserResult.from_result(resp)
