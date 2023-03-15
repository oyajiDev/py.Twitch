# -*- coding: utf-8 -*-
from urllib import parse
from typing import Optional, List


class Helix:
    def __init__(self, app_id:str, app_secret:str = None, user_token:str = None, scopes:Optional[List[str]] = [ "user:read:follows", "user:read:email" ]):
        scopes_encoded = "+".join([ parse.quote(scope) for scope in scopes ])

        if not user_token:
            url = f"https://id.twitch.tv/oauth2/authorize?client_id={app_id}&redirect_uri=http://localhost:3000&response_type=token&scope={scopes_encoded}"
            import webbrowser; webbrowser.open(url)
            user_token = input("user token: ")
            # raise RuntimeError(f"Please get token from twitch\n{url}")

        from .requests.analytics import AnalyticsRequest
        self.analytics = AnalyticsRequest(app_id, user_token)

        from .requests.channel import ChannelRequest
        self.channels = ChannelRequest(app_id, user_token)

        from .requests.stream import StreamRequest
        self.streams = StreamRequest(app_id, user_token)

        from .requests.user import UserRequest
        self.users = UserRequest(app_id, user_token)
