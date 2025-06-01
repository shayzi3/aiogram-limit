from datetime import datetime

from .abstract_storage import AbstractStorage
from ..schema import CallbackData



class MemoryStorage(AbstractStorage):
     storage: dict[str, CallbackData] = {}
     
     
     @classmethod
     async def get_data(
          cls, 
          callback_name: str
     ) -> bool | CallbackData:
          data = cls.storage.get(callback_name)
          return data if data else False
     
     
     @classmethod
     async def update_data_users(
          cls, 
          callback_name: str, 
          data: dict[str, datetime]
     ) -> None:
          cls.storage[callback_name].users.update(data)
          
          
     @classmethod
     async def set_data(
          cls,
          callback_name: str,
          callback_data: CallbackData
     ) -> None:
          cls.storage.update(
               {callback_name: callback_data}
          )
          