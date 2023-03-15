# -*- coding: utf-8 -*-


class RequestBase:
    def __init__(self, app_id:str, user_token:str):
        self.__app_id, self.__token = app_id, user_token

    @property
    def request_header(self) -> dict:
        return { "Client-Id": self.__app_id, "Authorization": f"Bearer {self.__token}" }
