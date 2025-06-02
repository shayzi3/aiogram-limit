import json

from dataclasses import dataclass
from datetime import timedelta, datetime


@dataclass
class CallbackData:
     all_users: bool
     expire: timedelta
     users: dict[str, datetime]
     
     
     def to_redis(self) -> str:
          self.expire = self.expire.seconds
          for key, value in self.users.items():
               self.users[key] = value.timestamp()
          return json.dumps(self.__dict__)
     
     
     @classmethod
     def from_redis(cls, data: str) -> "CallbackData":
          data = json.loads(data)
          
          data["expire"] = timedelta(seconds=data["expire"])
          for key, value in data["users"].items():
               data["users"][key] = datetime.fromtimestamp(value)
          return cls(**data)
     
     
     @staticmethod
     def _timedelta_from_str(time: str) -> timedelta:
          ...