# -*- coding: utf-8 -*-
import requests
from typing import Optional, Union
from datetime import datetime
from .base import RequestBase
from .._config import base_url
from ..models.analytics import ExtensionAnalyticsResult, GameAnalyticsResult
from ..errors import MissingScopeError



class AnalyticsRequest(RequestBase):
    def __init__(self, app_id:str, user_token:str):
        super().__init__(app_id, user_token)

    def get_extension_analytics(self, extension_id:Optional[str] = None, started_at:Optional[Union[datetime, str]] = None, ended_at:Optional[Union[datetime, str]] = None, first:Optional[int] = 20, after:Optional[str] = None) -> ExtensionAnalyticsResult:
        params = { "type": "overview_v2" }
        if extension_id:
            params["extension_id"] = extension_id
        if started_at:
            params["started_at"] = datetime.strftime(started_at, "%Y-%m-%dT%H:%M:%SZ") if isinstance(started_at, datetime) else started_at
        if ended_at:
            params["ended_at"] = datetime.strftime(ended_at, "%Y-%m-%dT%H:%M:%SZ") if isinstance(ended_at, datetime) else ended_at
        if first:
            params["first"] = first
        if after:
            params["after"] = after

        resp = requests.get(f"{base_url}/analytics/extensions", params = params, headers = self.request_header).json()
        if "error" in resp.keys() and resp["message"].startswith("Missing scope:"):
            raise MissingScopeError("scope is required: analytics:read:extensions")
        
        return ExtensionAnalyticsResult.from_result(resp)

    def get_game_analytics(self, game_id:Optional[str] = None, started_at:Optional[Union[datetime, str]] = None, ended_at:Optional[Union[datetime, str]] = None, first:Optional[int] = 20, after:Optional[str] = None) -> GameAnalyticsResult:
        params = { "type": "overview_v2" }
        if game_id:
            params["game_id"] = game_id
        if started_at:
            params["started_at"] = datetime.strftime(started_at, "%Y-%m-%dT%H:%M:%SZ") if isinstance(started_at, datetime) else started_at
        if ended_at:
            params["ended_at"] = datetime.strftime(ended_at, "%Y-%m-%dT%H:%M:%SZ") if isinstance(ended_at, datetime) else ended_at
        if first:
            params["first"] = first
        if after:
            params["after"] = after

        resp = requests.get(f"{base_url}/analytics/games", params = params, headers = self.request_header).json()
        if "error" in resp.keys() and resp["message"].startswith("Missing scope:"):
            raise MissingScopeError("scope is required: analytics:read:games")

        return GameAnalyticsResult.from_result(resp)
