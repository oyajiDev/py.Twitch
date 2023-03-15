# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import datetime


@dataclass
class DateRange:
    started_at:datetime
    ended_at:datetime

    @staticmethod
    def from_data(data:dict):
        return DateRange(
            started_at = datetime.strptime(data["started_at"], "%Y-%m-%dT%H:%M:%SZ"),
            ended_at = datetime.strptime(data["ended_at"], "%Y-%m-%dT%H:%M:%SZ")
        )
