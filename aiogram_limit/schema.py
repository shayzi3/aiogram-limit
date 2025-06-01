from dataclasses import dataclass
from datetime import timedelta, datetime
from typing import Any


@dataclass
class CallbackData:
     all_users: bool
     expire: timedelta
     users: dict[str, datetime]