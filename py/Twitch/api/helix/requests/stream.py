# -*- coding: utf-8 -*-
import requests
from typing import Optional, Union, List
from .base import RequestBase
from ..models.streams import StreamItem, StreamsResult
from .._config import base_url


class StreamRequest(RequestBase):
    def __init__(self, app_id:str, user_token:str):
        super().__init__(app_id, user_token)

    def get_stream(self, user_id:str = None, user_login:str = None, game_id:Optional[str] = None, type:Optional[str] = None, language:Optional[str] = None) -> Union[StreamItem, None]:
        params = {}
        if user_id:
            params["user_id"] = user_id
        if user_login:
            params["user_login"] = user_login
        if game_id:
            params["game_id"] = game_id
        if type:
            params["type"] = type
        if language:
            params["language"] = language

        resp = requests.get(f"{base_url}/streams", params = params, headers = self.request_header).json()
        if len(resp["data"]) == 0:
            return None
        
        return StreamItem.from_data(resp["data"][0])

    def get_streams(self, user_id:Optional[List[str]] = None, user_login:Optional[List[str]] = None, game_id:Optional[str] = None, type:Optional[str] = None, language:Optional[str] = None, first:Optional[int] = 20, before:Optional[str] = None, after:Optional[str] = None) -> StreamsResult:
        url = f"{base_url}/streams"
        if user_id:
            user_id_to_url = "&user_id=".join(user_id)
            url += f"?{user_id_to_url[1:]}"
        if user_login:
            user_login_to_url = "&user_login=".join(user_login)
            if url.endswith("/streams"):
                url += f"?{user_login_to_url[1:]}"
            else:
                url += user_login_to_url

        params = {}
        if game_id:
            params["game_id"] = game_id
        if type:
            params["type"] = type
        if language:
            params["language"] = language
        if first:
            params["first"] = first
        if before:
            params["before"] = before
        if after:
            params["after"] = after

        return StreamsResult.from_result(requests.get(url, params = params, headers = self.request_header).json())
