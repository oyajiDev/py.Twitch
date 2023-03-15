# -*- coding: utf-8 -*-
import requests
from typing import Optional, List
from .base import RequestBase
from .._config import base_url
from ..models.channels import FollowedChannelsResult, FollowedChannelItem


class ChannelRequest(RequestBase):
    def __init__(self, app_id:str, user_token:str):
        super().__init__(app_id, user_token)

    def get_followed_channels(self, user_id:str, broadcaster_id:Optional[str] = None, first:Optional[int] = 20, after:Optional[str] = None) -> FollowedChannelsResult:
        params = { "user_id": user_id }
        if broadcaster_id:
            params["broadcaster_id"] = broadcaster_id
        if first:
            params["first"] = first
        if after:
            params["after"] = after

        return FollowedChannelsResult.from_result(
            requests.get(f"{base_url}/channels/followed", params = params, headers = self.request_header).json()
        )

    def get_all_followed_channels(self, user_id:str) -> List[FollowedChannelItem]:
        resp = self.get_followed_channels(user_id, first = 100)
        after = resp.pagination.cursor

        while True:
            new_resp = self.get_followed_channels(user_id, first = 100, after = after)
            resp.data += new_resp.data
            after = new_resp.pagination.cursor

            if len(new_resp.data) < 100:
                break

        return resp.data
