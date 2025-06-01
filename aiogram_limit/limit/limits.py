from typing import Callable
from datetime import timedelta

from ..type import CallbackType
from ..schema import CallbackData
from ..storage import AbstractStorage, MemoryStorage


class Limits:
     def __init__(
          self, 
          messsage: str = "Request timeout",
          storage: AbstractStorage = MemoryStorage
     ):
          self.message = messsage
          self.storage = storage
     
     
     def __call__(
          self, 
          all_users: bool = False,
          seconds: int = 0,
          minutes: int = 0,
          hours: int = 0,
          weeks: int = 0,
          days: int = 0
     ) -> Callable[[CallbackType], CallbackType]:
          def wrapped(callback: CallbackType) -> CallbackType:
               callback_exists = self.storage.sync_get_data(callback.__name__)
               if callback_exists is False:
                    self.storage.sync_set_data(
                         callback_name=callback.__name__,
                         callback_data=CallbackData(
                              all_users=all_users,
                              expire=timedelta(
                                   days=days,
                                   weeks=weeks,
                                   hours=hours,
                                   minutes=minutes,
                                   seconds=seconds
                              ),
                              users={}
                         )
                    )
               return callback
          return wrapped