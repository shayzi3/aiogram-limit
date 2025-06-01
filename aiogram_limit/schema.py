from dataclasses import dataclass
from datetime import timedelta, datetime


@dataclass
class CallbackData:
     all_users: bool
     expire: timedelta
     users: dict[str, datetime]